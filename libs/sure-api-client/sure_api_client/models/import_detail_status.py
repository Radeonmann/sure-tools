from enum import Enum


class ImportDetailStatus(str, Enum):
    COMPLETE = "complete"
    FAILED = "failed"
    IMPORTING = "importing"
    PENDING = "pending"
    REVERTING = "reverting"
    REVERT_FAILED = "revert_failed"

    def __str__(self) -> str:
        return str(self.value)
