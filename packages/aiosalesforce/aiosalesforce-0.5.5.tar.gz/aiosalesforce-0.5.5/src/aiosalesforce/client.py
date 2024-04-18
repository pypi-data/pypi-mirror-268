import asyncio
import logging
import re
import warnings

from functools import cached_property, wraps
from typing import Any, AsyncIterator, Awaitable, Callable, Iterable, NoReturn

import httpx

from aiosalesforce import __version__
from aiosalesforce.auth import Auth
from aiosalesforce.bulk import BulkClientV2
from aiosalesforce.events import (
    Event,
    EventBus,
    RequestEvent,
    ResponseEvent,
)
from aiosalesforce.exceptions import SalesforceWarning, raise_salesforce_error
from aiosalesforce.retries import POLICY_DEFAULT, RetryPolicy
from aiosalesforce.sobject import SobjectClient
from aiosalesforce.utils import json_loads

logger = logging.getLogger(__name__)


class Salesforce:
    """
    Salesforce API client.

    Parameters
    ----------
    httpx_client : httpx.AsyncClient
        HTTP client.
    base_url : str
        Base URL of the Salesforce instance.
        Must be in the format:\n
        * Production    : https://[MyDomainName].my.salesforce.com
        * Sandbox       : https://[MyDomainName]-[SandboxName].sandbox.my.salesforce.com
        * Developer org : https://[MyDomainName].develop.my.salesforce.com\n
    auth : Auth
        Authentication object.
    version : str, optional
        Salesforce API version.
        By default, uses the latest version.
    event_hooks : Iterable[Callable[[Event], Awaitable[None] | None]], optional
        Functions or coroutines executed when an event occurs.
        Hooks are executed concurrently and order of execution is not guaranteed.
        All hooks must be thread-safe.
    retry_policy : RetryPolicy, optional
        Retry policy for requests.
        The default policy retries requests up to 3 times with exponential backoff
        and retries the following:\n
        * httpx Transport errors (excluding timeouts)
        * Server errors (5xx)
        * Row lock errors
        * Rate limit errors\n
        Set to None to disable retries.
    concurrency_limit : int, optional
        Maximum number of simultaneous requests to Salesforce.
        The default is 100.

    """

    httpx_client: httpx.AsyncClient
    base_url: str
    """Base URL in the format https://[subdomain(s)].my.salesforce.com"""
    auth: Auth
    version: str
    event_bus: EventBus
    retry_policy: RetryPolicy
    _semaphore: asyncio.Semaphore

    def __init__(
        self,
        httpx_client: httpx.AsyncClient,
        base_url: str,
        auth: Auth,
        version: str = "60.0",
        event_hooks: Iterable[Callable[[Event], Awaitable[None] | None]] | None = None,
        retry_policy: RetryPolicy | None = POLICY_DEFAULT,
        concurrency_limit: int = 100,
    ) -> None:
        self.httpx_client = httpx_client
        self.auth = auth

        # Validate version
        if not (match_ := re.fullmatch(r"^(v)?(\d+)(\.(0)?)?$", version)):
            raise ValueError(
                f"Invalid Salesforce API version: '{version}'. "
                f"A valid version should look like '60.0'."
            )
        self.version = f"{match_.groups()[1]}.0"

        # Validate url
        match_ = re.fullmatch(
            r"(https://[a-zA-Z0-9-]+(\.(sandbox|develop))?\.my\.salesforce\.com).*",
            base_url.strip(" ").lower(),
        )
        if not match_:
            raise ValueError(
                "\n".join(
                    [
                        f"Invalid Salesforce URL: {base_url}",
                        "Supported formats:",
                        "  Production    : https://[MyDomainName].my.salesforce.com",
                        "  Sandbox       : https://[MyDomainName]-[SandboxName].sandbox.my.salesforce.com",
                        "  Developer org : https://[MyDomainName].develop.my.salesforce.com",
                    ]
                )
            )
        self.base_url = str(match_.groups()[0])

        self.event_bus = EventBus(event_hooks)
        self.retry_policy = retry_policy or RetryPolicy()
        self._semaphore = asyncio.Semaphore(concurrency_limit)

    @wraps(httpx.AsyncClient.request)
    async def request(self, *args, **kwargs) -> httpx.Response:
        """
        Make an HTTP request to Salesforce.

        """
        request = self.httpx_client.build_request(*args, **kwargs)
        access_token = await self.auth.get_access_token(self)
        request.headers.update(
            {
                "Authorization": f"Bearer {access_token}",
                "User-Agent": f"aiosalesforce/{__version__}",
                "Sforce-Call-Options": f"client=aiosalesforce/{__version__}",
                "Sforce-Line-Ending": "LF",
            }
        )
        await self.event_bus.publish_event(
            RequestEvent(type="request", request=request)
        )
        retry_context = self.retry_policy.create_context()
        response = await retry_context.send_request_with_retries(
            httpx_client=self.httpx_client,
            event_bus=self.event_bus,
            semaphore=self._semaphore,
            request=request,
        )
        if response.status_code == 401:
            access_token = await self.auth.refresh_access_token(self)
            request.headers["Authorization"] = f"Bearer {access_token}"
            response = await retry_context.send_request_with_retries(
                httpx_client=self.httpx_client,
                event_bus=self.event_bus,
                semaphore=self._semaphore,
                request=request,
            )
        if not response.is_success:
            raise_salesforce_error(response)
        if "Warning" in response.headers:
            warnings.warn(response.headers["Warning"], SalesforceWarning)
        await self.event_bus.publish_event(
            ResponseEvent(type="response", response=response)
        )
        return response

    async def get_limits(self) -> dict[str, Any]:
        """
        Get Salesforce org limits.

        Returns
        -------
        dict
            Salesforce org limits.

        """
        response = await self.request(
            "GET", f"{self.base_url}/services/data/v{self.version}/limits"
        )
        return json_loads(response.content)

    async def query(
        self,
        query: str,
        include_all_records: bool = False,
    ) -> AsyncIterator[dict]:
        """
        Execute a SOQL query.

        Parameters
        ----------
        query : str
            SOQL query.
        include_all_records : bool, default False
            If True, includes all (active/deleted/archived) records.

        Yields
        -------
        dict
            Query result record.

        """
        operation = "query" if not include_all_records else "queryAll"

        next_url: str | None = None
        while True:
            if next_url is None:
                response = await self.request(
                    "GET",
                    f"{self.base_url}/services/data/v{self.version}/{operation}",
                    params={"q": query},
                )
            else:
                response = await self.request("GET", f"{self.base_url}{next_url}")
            response_json: dict = json_loads(response.content)
            for record in response_json["records"]:
                yield record
            next_url = response_json.get("nextRecordsUrl", None)
            if next_url is None:
                break

    @cached_property
    def sobject(self) -> SobjectClient:
        """
        Salesforce REST API sObject client.

        Use this client to perform CRUD operations on individual sObjects.

        """
        return SobjectClient(self)

    @cached_property
    def bulk_v1(self) -> NoReturn:
        """
        Get Salesforce Bulk API 1.0 client.

        Use this client to execute bulk ingest and query operations.

        """
        raise NotImplementedError("Bulk API v1 is currently not supported")

    @cached_property
    def bulk_v2(self) -> BulkClientV2:
        """
        Get Salesforce Bulk API 2.0 client.

        Use this client to execute bulk ingest and query operations.

        """
        return BulkClientV2(self)
