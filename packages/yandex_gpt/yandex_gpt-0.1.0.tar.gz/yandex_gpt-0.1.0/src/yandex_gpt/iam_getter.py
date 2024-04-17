from abc import ABC, abstractmethod
from .request_send import RequestHTTP
import datetime


class IAMException(Exception):
    pass


class IAMGetter(ABC):
    @abstractmethod
    def get_iam_token(self) -> str:
        """Get IAM token"""


class YandexApiGetterIAM(IAMGetter, RequestHTTP):
    """
    Swap OAuth token on IAM token
    """
    def __init__(self, oauth_token: str):
        self._oauth_token = oauth_token

    def _make_data(self) -> dict:
        return {"yandexPassportOauthToken": self._oauth_token}

    def _get_iam_token(self) -> str:
        response = self._make_request(
            method='POST',
            endpoint='/iam/v1/tokens',
            json=self._make_data(),
            headers=None
        )
        return response.json()['iamToken']

    def get_iam_token(self) -> str:
        return self._get_iam_token()

    @property
    def _host(self) -> str:
        return 'https://iam.api.cloud.yandex.net'


class YandexApiGetterIAMCache(YandexApiGetterIAM):
    """
    Swap OAuth token on IAM token with using cache
    """
    def __init__(self, oauth_token: str, hours_to_keep_token: int = 1):
        super().__init__(oauth_token=oauth_token)
        self._last_time_get_token_dttm = datetime.datetime.now()
        self._iam_token = self._get_iam_token()
        self._keep_token_minutes = hours_to_keep_token * 60

    def _is_token_still_actual(self) -> bool:
        time_diff_hours = (datetime.datetime.now() - self._last_time_get_token_dttm).total_seconds() // 60
        return time_diff_hours <= self._keep_token_minutes

    def get_iam_token(self) -> str:
        if not self._is_token_still_actual():
            self._iam_token = self._get_iam_token()
        return self._iam_token
