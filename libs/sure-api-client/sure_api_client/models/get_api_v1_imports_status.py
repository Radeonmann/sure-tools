from enum import Enum


class GetApiV1ImportsStatus(str, Enum):
    COMPLETE = "complete"
    FAILED = "failed"
    IMPORTING = "importing"
    PENDING = "pending"
    REVERTING = "reverting"
    REVERT_FAILED = "revert_failed"

    def __str__(self) -> str:
        return str(self.value)
