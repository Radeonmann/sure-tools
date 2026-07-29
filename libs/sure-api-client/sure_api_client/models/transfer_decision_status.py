from enum import Enum


class TransferDecisionStatus(str, Enum):
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
