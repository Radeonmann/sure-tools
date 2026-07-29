from enum import Enum


class GetApiV1TransactionsType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"

    def __str__(self) -> str:
        return str(self.value)
