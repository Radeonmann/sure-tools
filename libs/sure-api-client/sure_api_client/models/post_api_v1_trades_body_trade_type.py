from enum import Enum


class PostApiV1TradesBodyTradeType(str, Enum):
    BUY = "buy"
    DEPOSIT = "deposit"
    DIVIDEND = "dividend"
    INTEREST = "interest"
    SELL = "sell"
    WITHDRAWAL = "withdrawal"

    def __str__(self) -> str:
        return str(self.value)
