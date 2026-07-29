from enum import Enum


class PostApiV1ImportSessionsBodyType(str, Enum):
    SUREIMPORT = "SureImport"

    def __str__(self) -> str:
        return str(self.value)
