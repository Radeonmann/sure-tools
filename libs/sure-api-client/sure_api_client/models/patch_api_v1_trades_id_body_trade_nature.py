from enum import Enum


class PatchApiV1TradesIdBodyTradeNature(str, Enum):
    INFLOW = "inflow"
    OUTFLOW = "outflow"

    def __str__(self) -> str:
        return str(self.value)
