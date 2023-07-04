import json
import requests
from vk_api.vk_models import Message
import logging

ACCESS_TOKEN: str
with open("access_token") as token_file:
    ACCESS_TOKEN = token_file.read()

URL = "https://api.vk.com/method/{}?v=5.131&access_token=" + ACCESS_TOKEN


class EndOfDialogueException(BaseException):
    pass


class APIException(BaseException):
    pass


def messages_history_generator(
    *,
    offset: int,
    count: int,
    user_id: int,
    rev: int = 1,
):
    offset = offset

    while True:
        response = requests.post(
            URL.format("messages.getHistory"),
            params={
                "offset": offset,
                "count": count,
                "user_id": user_id,
                "rev": rev,
            }
        )

        if response.status_code != 200:
            raise APIException()

        if not json.loads(response.content)["response"]["items"]:
            raise EndOfDialogueException()

        for item in json.loads(response.content)["response"]["items"]:
            yield Message(**item)

        offset += count
