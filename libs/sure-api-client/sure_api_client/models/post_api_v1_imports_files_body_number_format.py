from enum import Enum


class PostApiV1ImportsFilesBodyNumberFormat(str, Enum):
    VALUE_0 = "1,234.56"
    VALUE_1 = "1.234,56"
    VALUE_2 = "1 234,56"
    VALUE_3 = "1,234"

    def __str__(self) -> str:
        return str(self.value)
