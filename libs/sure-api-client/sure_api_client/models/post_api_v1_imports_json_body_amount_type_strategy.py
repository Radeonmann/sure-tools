from enum import Enum


class PostApiV1ImportsJsonBodyAmountTypeStrategy(str, Enum):
    CUSTOM_COLUMN = "custom_column"
    SIGNED_AMOUNT = "signed_amount"

    def __str__(self) -> str:
        return str(self.value)
