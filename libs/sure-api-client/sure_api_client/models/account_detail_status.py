from enum import Enum


class AccountDetailStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    DRAFT = "draft"
    PENDING_DELETION = "pending_deletion"

    def __str__(self) -> str:
        return str(self.value)
