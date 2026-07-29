from enum import Enum


class GetApiV1SecuritiesKind(str, Enum):
    CASH = "cash"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
