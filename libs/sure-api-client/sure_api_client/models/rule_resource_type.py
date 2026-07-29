from enum import Enum


class RuleResourceType(str, Enum):
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
