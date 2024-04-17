from dataclasses import dataclass
from typing import List, Dict


@dataclass
class YandexGPTModels:
    YANDEX_GPT_PRO = 'gpt://{folder_id}/yandexgpt/latest'
    YANDEX_GPT_LITE = 'gpt://{folder_id}/yandexgpt-lite/latest'
    YANDEX_GPT_SUMMARIZE = 'gpt://{folder_id}/summarization/latest'
    YANDEX_GPT_CUSTOM_MODEL = 'ds://{custom_model_id}'


@dataclass
class Message:
    text: str

    def as_json(self):
        return self.__dict__


class UserMessage(Message):
    role: str = 'user'


class SystemMessage(Message):
    role: str = 'system'


class AssistantMessage(Message):
    role: str = 'assistant'


class Messages:
    _messages: List[Message] = []

    def __init__(self, *messages):
        if messages.__len__() > 0:
            self.add_new_messages(*messages)

    @staticmethod
    def _validate(obj: any) -> None:
        if not isinstance(obj, Message):
            raise TypeError('Object must be subclass of schemas.Message')

    def add_new_messages(self, *messages) -> None:
        for message in messages:
            self._validate(message)
            self._messages.append(message)

    @property
    def messages(self) -> List[Message]:
        return self._messages

    @property
    def messages_as_json(self) -> List[Dict[str, str]]:
        messages_json = []
        for message in self._messages:
            messages_json.append(message.as_json())
        return messages_json


@dataclass
class Alternative:
    message: Message
    status: str


@dataclass
class UsageTokens:
    input_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class YandexGPTResponse:
    alternatives: List[Alternative]
    model_version: str
    usage: UsageTokens

    @classmethod
    def from_json(cls, data: dict):
        data = data['result']

        alternatives = data['alternatives']
        alternative_to_init = []

        for alternative in alternatives:
            role = alternative['message']['role']

            message = None
            if role == 'assistant':
                message = AssistantMessage(alternative['message']['text'])
            if role == 'system':
                message = SystemMessage(alternative['message']['text'])
            if role == 'user':
                message = UserMessage(alternative['message']['text'])

            alternative_to_init.append(
                Alternative(message, alternative['status'])
            )

        usage = UsageTokens(*[int(x) for x in data['usage'].values()])

        return cls(alternative_to_init, data['modelVersion'], usage)
