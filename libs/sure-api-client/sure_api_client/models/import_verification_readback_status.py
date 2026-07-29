from enum import Enum


class ImportVerificationReadbackStatus(str, Enum):
    FAILED = "failed"
    MATCHED = "matched"
    MISMATCH = "mismatch"
    NOT_VERIFIED = "not_verified"
    REVERTED = "reverted"

    def __str__(self) -> str:
        return str(self.value)
