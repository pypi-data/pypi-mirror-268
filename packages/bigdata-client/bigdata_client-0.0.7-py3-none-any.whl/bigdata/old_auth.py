import datetime
from typing import Optional

import requests

from bigdata.jwt import get_jwt_date
from bigdata.settings import settings
from bigdata.user_agent import get_user_agent


class Auth:
    """
    Class that performs the authentication logic, and wraps all the http calls
    so that it can handle the token autorefresh when needed.
    """

    def __init__(self):
        self.api_endpoint: str = settings.AUTH_LOGIN_FORM_ENDPOINT
        self.jwt_refresh_token: Optional[str] = None
        self.x_csrf_token: Optional[str] = None
        self._session = requests.session()

        # The field `is_datetime_in_sync` marks if the datetime is in sync with
        # the server If it's not, the token will not be refreshed as soon as it
        # expires, and we will wait until the request fails to refresh it
        # Currently, we only refresh the JWT after the first request fails
        # without looking at the exp, but we could do that so that we don't
        # make unnecessary requests.
        # TODO: Delete this attribute and related methods if not used
        self.is_datetime_in_sync = False

    @classmethod
    def from_username_and_password(cls, username: str, password: str) -> "Auth":
        auth = Auth()
        auth.login(username, password)
        return auth

    def login(self, username=None, password=None):
        """
        Authenticates, getting the jwt and refresh tokens from the username
        and password.
        """
        if self.jwt_refresh_token is not None:
            raise ValueError("Already logged in")
        # The payload says "email" but it accepts usernames as well
        payload = {"email": username, "password": password}
        headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "origin": "https://bigdata.com",
        }
        response = self._session.post(
            "https://bigdata.com/api/login",
            headers=headers,
            json=payload,
        )
        self.x_csrf_token = response.headers["x-csrf-token"]
        self._handle_auth_response(response)

    def refresh_jwt(self):
        """Refreshes the jwt token"""
        if self.jwt_refresh_token is None:
            raise ValueError("Login first")
        headers = {
            "content-type": "application/json",
            "accept": "application/json",
            "origin": "https://bigdata.com",
            "x-csrf-token": self.x_csrf_token,
            "x-refresh-token": self.jwt_refresh_token,
            "user-agent": get_user_agent(settings.PACKAGE_NAME),
        }
        response = self._session.post(
            "https://bigdata.com/api/refresh",
            headers=headers,
        )
        self._handle_auth_response(response)

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        json=None,
    ):
        """Makes an HTTP request, handling the token refresh if needed"""
        headers = headers or {}
        headers["origin"] = "https://bigdata.com"
        headers["referer"] = "https://bigdata.com/"
        # if "content-type" not in headers:
        # We may have to conditionally set the content type when uploading files
        headers["content-type"] = "application/json"
        headers["accept"] = "application/json"
        headers["x-csrf-token"] = self.x_csrf_token
        headers["user-agent"] = get_user_agent(settings.PACKAGE_NAME)
        # The requet method has other arguments but we are not using them currently
        response = self._session.request(
            method=method, url=url, params=params, data=data, headers=headers, json=json
        )
        if response.status_code == 401:
            self.refresh_jwt()
            # Retry the request
            response = self._session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                headers=headers,
                json=json,
            )
        return response

    def _handle_auth_response(self, response):
        response.raise_for_status()
        self.jwt_refresh_token = response.json()["refresh"]
        self.is_datetime_in_sync = self._is_jwt_recent(self.jwt_refresh_token)

    @staticmethod
    def _is_jwt_recent(jwt_token: str, max_seconds=30):
        now = datetime.datetime.now(datetime.timezone.utc)
        issued_at = get_jwt_date(jwt_token, "iat")
        time_diff = abs((now - issued_at).total_seconds())
        if time_diff < max_seconds:
            return True
        else:
            return False
