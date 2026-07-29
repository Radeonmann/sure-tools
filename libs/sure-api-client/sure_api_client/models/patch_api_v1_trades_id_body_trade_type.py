from enum import Enum


class PatchApiV1TradesIdBodyTradeType(str, Enum):
    BUY = "buy"
    DEPOSIT = "deposit"
    DIVIDEND = "dividend"
    INTEREST = "interest"
    SELL = "sell"
    WITHDRAWAL = "withdrawal"

    def __str__(self) -> str:
        return str(self.value)
