from enum import Enum


class ResetStatusResponseStatus(str, Enum):
    COMPLETE = "complete"
    DATA_REMAINING = "data_remaining"

    def __str__(self) -> str:
        return str(self.value)
