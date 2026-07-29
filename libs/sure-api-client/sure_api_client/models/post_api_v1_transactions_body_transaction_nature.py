from enum import Enum


class PostApiV1TransactionsBodyTransactionNature(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"
    INFLOW = "inflow"
    OUTFLOW = "outflow"

    def __str__(self) -> str:
        return str(self.value)
