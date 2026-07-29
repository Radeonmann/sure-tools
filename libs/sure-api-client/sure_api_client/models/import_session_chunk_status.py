from enum import Enum


class ImportSessionChunkStatus(str, Enum):
    COMPLETE = "complete"
    FAILED = "failed"
    IMPORTING = "importing"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
