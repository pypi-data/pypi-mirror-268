from .iam_getter import YandexApiGetterIAM, YandexApiGetterIAMCache, IAMGetter
from .request_send import RequestHTTP
from .schemas import YandexGPTModels, Messages, YandexGPTResponse
from typing import Optional


class YandexGPT(RequestHTTP):
    def __init__(
            self,
            oauth_token: str,
            folder_id: str,
            use_cache_for_iam: bool = True,
            disable_logging: bool = True,
            gpt_model: str = YandexGPTModels.YANDEX_GPT_PRO,
            custom_model_id: Optional[str] = None,
            temperature: float = 0.3,
            max_tokens: int = 2000
    ):
        """
        Main class for connecting to YandexGPT. For working you need folder-id and OAuth token from yandex api
        https://yandex.cloud/ru/docs/foundation-models/api-ref/authentication

        :param oauth_token: OAuth Token
        :param folder_id: Folder id
        :param use_cache_for_iam: Is need to use cache for getting IAM token
        :param disable_logging: Is need to disable
        :param gpt_model: Version of GPT model
        :param custom_model_id: Custom model id if you're trying to use model from DataSphere
        :param temperature: Temperature of GPT model
        :param max_tokens: Limit for tokens
        """
        self._iam_getter = YandexApiGetterIAMCache if use_cache_for_iam else YandexApiGetterIAM
        self._iam_getter: IAMGetter = self._iam_getter(oauth_token)
        self._folder_id = folder_id
        self._custom_model_id = custom_model_id
        self._gpt_model = gpt_model
        self._temperature = temperature
        self._max_tokens = max_tokens
        self._disable_logging = disable_logging

    @property
    def _host(self) -> str:
        return 'https://llm.api.cloud.yandex.net'

    def _get_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self._iam_getter.get_iam_token()}',
            'x-data-logging-enabled': 'true' if self._disable_logging else 'false'
        }

    def _make_data(self, messages: Messages) -> dict:
        return {
            "modelUri": self._gpt_model.format(folder_id=self._folder_id, custom_model_id=self._custom_model_id),
            "completionOptions": {
                "stream": False,
                "temperature": self._temperature,
                "maxTokens": str(self._max_tokens)
            },
            'messages': messages.messages_as_json
        }

    def completion(self, messages: Messages) -> YandexGPTResponse:
        """
        Method for getting answer from YandexGPT API
        :param messages: messages with context for GPT
        :return: Response from YandexGPT API
        """
        response = self._make_request(
            method='POST',
            endpoint='/foundationModels/v1/completion',
            json=self._make_data(messages),
            headers=self._get_headers()
        )
        return YandexGPTResponse.from_json(response.json())
