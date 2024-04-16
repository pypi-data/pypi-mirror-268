from abc import ABC, abstractmethod
from time import sleep

import requests
import urllib3

from netorca_sdk.config import API_VERSION, AUTH_ENDPOINT, RETRY_TIMES, TEAM_ENDPOINT
from netorca_sdk.exceptions import (
    NetorcaAPIError,
    NetorcaAuthenticationError,
    NetorcaException,
    NetorcaGatewayError,
    NetorcaNotFoundError,
    NetorcaServerUnavailableError,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AbstractNetorcaAuth(ABC):
    @abstractmethod
    def get(self, *args, **kwargs):
        ...

    @abstractmethod
    def post(self, *args, **kwargs):
        ...

    @abstractmethod
    def put(self, *args, **kwargs):
        ...

    @abstractmethod
    def patch(self, *args, **kwargs):
        ...

    @abstractmethod
    def delete(self, *args, **kwargs):
        ...

    @abstractmethod
    def options(self, *args, **kwargs):
        ...


class NetorcaAuth(AbstractNetorcaAuth):
    def __init__(self, fqdn, username=None, password=None, api_key=None):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.fqdn = fqdn
        self.headers = {"content-type": "application/json"}

        if self.username and self.password:
            self.token = self.get_auth_token()
            self.headers["Authorization"] = f"Token {self.token}"
        elif self.api_key:
            self.headers["Authorization"] = f"Api-Key {self.api_key}"
        else:
            raise NetorcaException("Failed to authenticate. You must provide either (username and password) or API KEY")

    def get(self, *args, **kwargs):
        url = kwargs.get("url")
        filters = kwargs.get("filters")
        if filters:
            url = f"{url}?{'&'.join([f'{k}={v}' for k, v in filters.items()])}"
        authentication_required = kwargs.get("authentication_required", False)

        if not url:
            raise NetorcaException("URL not provided!")

        for retry in range(RETRY_TIMES):
            if authentication_required:
                response = requests.get(url=url, headers=self.headers, verify=False)
            else:
                response = requests.get(url=url, verify=False)
            if 200 <= response.status_code < 500:
                return response
            sleep(retry)
        raise NetorcaException(
            f"Failed to send GET request. GET details: {args, kwargs}. Response status_code: {response.status_code}"
        )

    def post(self, *args, **kwargs):
        url = kwargs.get("url")
        data = kwargs.get("data")
        authentication_required = kwargs.get("authentication_required", False)

        if not url or not data:
            raise NetorcaException("URL or data not provided!")

        if authentication_required:
            response = requests.post(url=url, data=data, headers=self.headers, verify=False)
        else:
            response = requests.post(url=url, data=data, verify=False)

        if 200 <= response.status_code < 500:
            return response
        raise NetorcaException(
            f"Failed to send POST request. POST details: {args, kwargs}.  Response status_code: {response.status_code}"
        )

    def put(self, *args, **kwargs):
        url = kwargs.get("url")
        data = kwargs.get("data")
        authentication_required = kwargs.get("authentication_required", False)

        if not url or not data:
            raise NetorcaException("URL or data not provided!")

        if authentication_required:
            response = requests.put(url=url, data=data, headers=self.headers, verify=False)
        else:
            response = requests.put(url=url, data=data, verify=False)
        if 200 <= response.status_code < 500:
            return response
        raise NetorcaException(
            f"Failed to send PUT request. PUT details: {args, kwargs}.  Response status_code: {response.status_code}"
        )

    def patch(self, *args, **kwargs):
        url = kwargs.get("url")
        data = kwargs.get("data")
        authentication_required = kwargs.get("authentication_required", False)

        if not url or not data:
            raise NetorcaException("URL or data not provided!")

        if authentication_required:
            response = requests.patch(url=url, data=data, headers=self.headers, verify=False)
        else:
            response = requests.patch(url=url, data=data, verify=False)

        if 200 <= response.status_code < 500:
            return response
        raise NetorcaException(
            f"Failed to send PATCH request. PATCH details: {args, kwargs}.  Response status_code: {response.status_code}"
        )

    def delete(self, *args, **kwargs):
        NetorcaException("Not implemented.")

    def options(self, *args, **kwargs):
        url = kwargs.get("url")
        authentication_required = kwargs.get("authentication_required", False)

        if not url:
            raise NetorcaException("URL not provided!")

        for retry in range(RETRY_TIMES):
            if authentication_required:
                response = requests.options(url=url, headers=self.headers, verify=False)
            else:
                response = requests.options(url=url, verify=False)
            if 200 <= response.status_code < 500:
                return response
            sleep(retry)
        raise NetorcaException(
            f"Failed to send OPTIONS request. OPTIONS details: {args, kwargs}.  Response status_code: {response.status_code}"
        )

    def get_auth_token(self) -> str:
        AUTH_URL = f"{self.fqdn}{API_VERSION}{AUTH_ENDPOINT}"

        data = {"username": self.username, "password": self.password}
        response = self.post(url=AUTH_URL, data=data, verify=False)
        if response.status_code == 200:
            return response.json()["token"]
        raise NetorcaException(f"Authentication failed due response status_code: {response.status_code}")

    def refresh_auth_token(self):
        return self.get_auth_token()

    def get_teams_info(self) -> list:
        """Get team info for given user"""
        TEAM_URL = f"{self.fqdn}{TEAM_ENDPOINT}"
        response = self.get(url=TEAM_URL, authentication_required=True)
        if response.status_code == 200:
            return response.json()["results"]
        elif response.status_code == 403:
            raise NetorcaAPIError("Access denied.")
        elif response.status_code == 404:
            raise NetorcaNotFoundError("endpoint not found.")
        elif response.status_code == 401:
            raise NetorcaAuthenticationError("Authentication failed.")
        elif response.status_code == 502:
            raise NetorcaGatewayError("Load balancer or webserver is down.")
        elif response.status_code == 503:
            raise NetorcaServerUnavailableError("Server is temporarily unavailable.")
        else:
            raise NetorcaAPIError(f"Error {response.status_code}")

    def __str__(self):
        return f"Username: {self.username}, netorca instance: {self.fqdn}."

    def __repr__(self):
        return f"Username: {self.username}, netorca instance: {self.fqdn}."
