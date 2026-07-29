from enum import Enum


class MessageType(str, Enum):
    ASSISTANT_MESSAGE = "assistant_message"
    USER_MESSAGE = "user_message"

    def __str__(self) -> str:
        return str(self.value)
