"""Base class for API clients."""

from dataclasses import dataclass, field
from datetime import datetime
import functools
import os
from posixpath import join
from typing import Callable, Optional

import requests
from requests.adapters import HTTPAdapter, Retry

# We are uploading files we want to retry when we receive certain error codes
RETRY_TOTAL = 7
BACKOFF_FACTOR = 2
STATUS_FORCELIST = [502, 503, 504]


@dataclass
class BaseApi:  # pylint: disable=too-many-instance-attributes
    """
    Base class for clients to QCi APIs, especially the authorization layer.

    :param url: url basepath to API endpoint, including scheme, if None, then falls back
        to QCI_API_URL environment variable
    :param api_token: refresh token for authenticating to API, if None, then falls back
        to QCI_TOKEN environment variable
    :param access_tokens: url path fragment to specify access-tokens API endpoint
    :param set_bearer_token_on_init: flag to turn on/off access token retrieval on
        object initialization
    :param timeout: number of seconds before timing out requests, None waits indefinitely
    :param debug: flag to turn on/off debug prints
    """

    url: Optional[str] = None
    # Hide sensistive info to prevent accidental logging when printing client objects.
    api_token: Optional[str] = field(default=None, repr=False)
    access_tokens: str = "auth/v1/access-tokens"
    set_bearer_token_on_init: bool = True
    # Request timeout in seconds for connection & read. None for infinite timeout.
    timeout: Optional[float] = None
    debug: bool = False

    def __post_init__(self):
        self.url = self.url if self.url else os.getenv("QCI_API_URL")

        if self.url is None:
            raise AssertionError(
                "QCI_API_URL environment variable is empty. Specify url or add the "
                "necessary environment variable"
            )

        # removing trailling / so can add paths simply
        self.url.rstrip("/")

        self.api_token = self.api_token if self.api_token else os.getenv("QCI_TOKEN")

        if self.api_token is None:
            raise AssertionError(
                "QCI_TOKEN environment variable is empty. Specify api_token or add the "
                "necessary environment variable"
            )

        self.session = requests.Session()
        retries = Retry(
            total=RETRY_TOTAL,
            backoff_factor=BACKOFF_FACTOR,
            status_forcelist=STATUS_FORCELIST,
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        self._bearer_info = {}

        if self.set_bearer_token_on_init:
            self.set_bearer_token()

    @property
    def auth_url(self) -> str:
        """Return the URL used for authorization."""
        return join(self.url, self.access_tokens)

    @property
    def headers_without_token(self):
        """Headers without cached bearer token."""
        headers = {
            "Content-Type": "application/json",
            "Connection": "close",
        }

        if self.timeout is not None:
            # Provide client's request timeout to server (latency provides some buffer).
            headers.update({"X-Request-Timeout-Nano": str(int(10**9 * self.timeout))})

        return headers

    @property
    def headers(self):
        """Headers with cached bearer token."""
        headers = self.headers_without_token
        headers["Authorization"] = f"Bearer {self._bearer_info.get('access_token', '')}"

        return headers

    @property
    def headers_without_connection_close(self):
        """Headers with cached bearer token, but without connection closing."""
        headers = self.headers
        headers.pop("Connection", None)

        return headers

    @classmethod
    def _check_response_error(cls, response: requests.Response) -> None:
        """
        Single place to update error check and message for API calls
        :param response: a response from any API call using the requests package
        """
        try:
            # The requests package does special handling here, so build off of this.
            response.raise_for_status()
        except requests.HTTPError as err:
            # Include response body in exception message to aid user understanding.
            raise requests.HTTPError(
                str(err) + f" with response body: {response.text}"
            ) from err

    def get_bearer_token(self) -> requests.Response:
        """Request new bearer token. (Not cached here, see set_bearer_token.)"""
        payload = {"refresh_token": self.api_token}

        response = self.session.request(
            "POST",
            self.auth_url,
            json=payload,
            headers=self.headers_without_token,
            timeout=self.timeout,
        )

        self._check_response_error(response)

        return response

    def set_bearer_token(self) -> None:
        """Set bearer token from request."""
        resp = self.get_bearer_token()
        self._bearer_info = resp.json()

    def is_bearer_token_expired(self) -> bool:
        """Is current time > 'expires' time."""
        if "expires_at_rfc3339" not in self._bearer_info:
            return True

        expiration = datetime.strptime(
            self._bearer_info["expires_at_rfc3339"], "%Y-%m-%dT%H:%M:%SZ"
        )
        seconds_to_expiration = (expiration - datetime.utcnow()).total_seconds()

        # adding 10 second buffer for expiration
        return seconds_to_expiration < 10

    @staticmethod
    def refresh_token(func) -> Callable:
        """Return a wrapper function that can check an auth token."""

        @functools.wraps(func)
        def check_token(api, *args, **kwargs):
            # Because the decorated function is receiving 'self', we need to pass this
            # additional argument along in the 'api' arg.
            is_expired = api.is_bearer_token_expired()
            # expired, reset the token
            if is_expired:
                api.set_bearer_token()
                return func(api, *args, **kwargs)
            # still have time on the token, so just pass the wrapped func through
            return func(api, *args, **kwargs)

        return check_token
