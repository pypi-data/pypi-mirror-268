"""
Module for simple connecting to YandexGPT Api

Example to use:
from yandex_gpt import YandexGPT, Messages, SystemMessage, UserMessage

yandex_gpt_client = YandexGPT(
    OAUTH_TOKEN,
    FOLDER_ID
)

chat = Messages(
    SystemMessage('Ты в диалоге с пользователем. Отвечай на все его запросы'),
    UserMessage('Привет! Посоветуй фильм на вечер')
)

response = yandex_gpt_client.completion(chat)
print(response.alternatives[0].message)
"""

from .interface import YandexGPT
from .schemas import Messages, UserMessage, SystemMessage, AssistantMessage
from .schemas import YandexGPTModels
