from pydantic import BaseModel

from datetime import datetime

from typing import Optional
from typing import List

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_sender_name(*, from_id: int):
    match from_id:
        case 441515260:
            return "Дишка"
        case 678562910:
            return "Доля"
        case _:
            return from_id


class Message(BaseModel):
    id: int = None
    from_id: int
    date: datetime
    text: str
    attachments: List[dict]
    fwd_messages: Optional[List['Message']] = None
    reply_message: Optional['Message'] = None

    class Config:
        extra = "ignore"

    def represent(self):
        return get_sender_name(from_id=self.from_id) + ' ' + self.date.strftime(DATETIME_FORMAT) + '\n' + self.text

    def __str__(self):
        return self.represent()

    def __repr__(self):
        return "\n\n" + self.represent()
