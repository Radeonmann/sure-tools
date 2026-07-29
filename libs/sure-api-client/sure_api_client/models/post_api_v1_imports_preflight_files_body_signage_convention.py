from enum import Enum


class PostApiV1ImportsPreflightFilesBodySignageConvention(str, Enum):
    INFLOWS_NEGATIVE = "inflows_negative"
    INFLOWS_POSITIVE = "inflows_positive"

    def __str__(self) -> str:
        return str(self.value)
