from enum import Enum


class SyncResourceStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    STALE = "stale"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
