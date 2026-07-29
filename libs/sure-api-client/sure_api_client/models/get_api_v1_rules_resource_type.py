from enum import Enum


class GetApiV1RulesResourceType(str, Enum):
    TRANSACTION = "transaction"

    def __str__(self) -> str:
        return str(self.value)
