from enum import Enum


class SecurityKind(str, Enum):
    CASH = "cash"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
