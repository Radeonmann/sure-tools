from enum import Enum


class RuleRunExecutionType(str, Enum):
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
