from enum import Enum


class PostApiV1ImportsPreflightJsonBodySignageConvention(str, Enum):
    INFLOWS_NEGATIVE = "inflows_negative"
    INFLOWS_POSITIVE = "inflows_positive"

    def __str__(self) -> str:
        return str(self.value)
