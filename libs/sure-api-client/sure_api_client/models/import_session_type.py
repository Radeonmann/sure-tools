from enum import Enum


class ImportSessionType(str, Enum):
    SUREIMPORT = "SureImport"

    def __str__(self) -> str:
        return str(self.value)
