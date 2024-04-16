import json
import logging
import os

import requests
from ratelimit import RateLimitException, limits, sleep_and_retry

from .domain import Domains
from .groups import Groups
from .record import Records
from .utils.make_async import make_methods_async

DEFAULT_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

DEFAULT_BASE_URL = "https://apiv2.mtgsy.net/api/v1"


@make_methods_async
class BaseClient:
    def __init__(self, username=None, apikey=None, url=DEFAULT_BASE_URL) -> None:
        if not username:
            username = os.environ.get("CLOUDFLOOR_USERNAME", "").strip()
        if not username:
            raise Exception("username required")

        if not apikey:
            apikey = os.environ.get("CLOUDFLOOR_APIKEY", "").strip()
        if not apikey:
            raise Exception("username required")
        self._username = username
        self._apikey = apikey
        self._url = url.rstrip("/")

    def request(self, method, url, data=None, timeout=None):
        if not url.startswith("/"):
            raise Exception(
                f"url '{url}' is invalid: must be a path with a leading '/' "
            )
        if not data:
            data = {}
        request_data = {
            **data,
            "username": self._username,
            "apikey": self._apikey,
        }
        url = f"{self._url}{url}"
        error_message = "Unknown error"
        response = requests.request(
            method,
            url,
            headers=DEFAULT_HEADERS,
            data=json.dumps(request_data),
            allow_redirects=True,
            timeout=timeout,
        )
        res = response.json()
        error = res.get("error")
        if error:
            logging.debug(error)
            error_message = error.get("description", "Unknown error")
            if "Too Many Requests" in error_message:
                raise RateLimitException(error_message, 10)
            raise Exception(error_message)
        return res.get("data")

    # https://stackoverflow.com/questions/401215/how-to-limit-rate-of-requests-to-web-services-in-python
    @sleep_and_retry
    @limits(calls=120, period=60)
    def get(self, url, data=None, timeout=None):
        return self.request("GET", url, data=data, timeout=timeout)

    @sleep_and_retry
    @limits(calls=30, period=60)
    def post(self, url, data=None, timeout=None):
        return self.request("POST", url, data=data, timeout=timeout)

    @sleep_and_retry
    @limits(calls=60, period=60)
    def patch(self, url, data=None, timeout=None):
        return self.request("PATCH", url, data=data, timeout=timeout)

    def delete(self, url, data=None, timeout=None):
        return self.request("DELETE", url, data=data, timeout=timeout)


class Client(BaseClient):
    def __init__(self, username=None, apikey=None, url=DEFAULT_BASE_URL) -> None:
        super().__init__(username=username, apikey=apikey, url=url)
        self.records = Records(self)
        self.domains = Domains(self)
        self.groups = Groups(self)

    def yield_all_domains_records(self, zone_enabled=None):
        domains = self.domains.list(zone_enabled=zone_enabled)
        for d in domains:
            records = self.records.list(d.domainname)
            yield d, records

    def all_domains_records(self, zone_enabled=None):
        return dict(self.yield_all_domains_records(zone_enabled=zone_enabled))
