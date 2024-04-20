import logging

import requests
import curlify
from requests import Response


def session_management(func):
    def wrapper(*args, **kwargs):
        client = args[0]
        client.open_session()  # Open session before making requests
        try:
            return func(*args, **kwargs)
        finally:
            client.close_session()  # Close session after making requests

    return wrapper


class RestApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = None
        self.logger = logging.getLogger(__name__)

    def open_session(self):
        self.session = requests.Session()

    def close_session(self):
        if self.session:
            self.session.close()

    @session_management
    def _make_request(self, method, path, params=None, data=None, json_data=None, headers=None):
        url = self.base_url + path
        self.logger.info(f"Making {method} request to {url}")

        response = self.session.request(method, url, params=params, data=data, json=json_data, headers=headers)
        curl = curlify.to_curl(response.request)

        self.logger.info(curl)
        self.logger.info(f"Response received for {method} request to {url} with status code {response.status_code}")
        self.logger.info(response.json())
        response.raise_for_status()
        return response

    def get(self, path, params=None, headers=None) -> Response:
        return self._make_request("GET", path, params=params, headers=headers)

    def post(self, path, data=None, json_data=None, headers=None) -> Response:
        return self._make_request("POST", path, data=data, json_data=json_data, headers=headers)

    def put(self, path, data=None, json_data=None, headers=None) -> Response:
        return self._make_request("PUT", path, data=data, json_data=json_data, headers=headers)

    def delete(self, path, headers=None) -> Response:
        return self._make_request("DELETE", path, headers=headers)
