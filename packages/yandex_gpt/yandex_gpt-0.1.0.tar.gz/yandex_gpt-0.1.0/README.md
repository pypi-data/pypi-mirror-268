## (Module for simple connecting to YandexGPT Api)

Example to use:
```python
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
```

It is possible to replace the model like this
```python
from yandex_gpt import YandexGPT, YandexGPTModels

yandex_gpt_client = YandexGPT(
    OAUTH_TOKEN,
    FOLDER_ID,
    gpt_model=YandexGPTModels.YANDEX_GPT_LITE
)
```