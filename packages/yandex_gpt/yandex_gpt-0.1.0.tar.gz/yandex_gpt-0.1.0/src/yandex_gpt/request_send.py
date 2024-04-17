import requests
from requests import RequestException, Response
from abc import ABC, abstractmethod


class YandexApiException(RequestException):
    pass


class RequestMaker(ABC):
    """
    Abstract class for make requests to yandex hosts
    """
    @abstractmethod
    def _make_request(self, *args, **kwargs) -> Response:
        """Request maker"""


class RequestHTTP(RequestMaker, ABC):
    @staticmethod
    def _convert_response_with_error(response: Response) -> str:
        return f'Request error with status code {response.status_code}\n{response.text}'

    def _make_request(self, method: str, endpoint: str, headers=None, data=None, json=None) -> Response:
        url = f'{self._host}{endpoint}'
        response = requests.request(
            method=method,
            url=url,
            data=data,
            headers=headers,
            json=json
        )
        if response.status_code != 200:
            raise YandexApiException(self._convert_response_with_error(response))
        return response

    @property
    @abstractmethod
    def _host(self) -> str:
        pass
