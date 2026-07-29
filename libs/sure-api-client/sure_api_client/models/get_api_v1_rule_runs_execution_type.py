from enum import Enum


class GetApiV1RuleRunsExecutionType(str, Enum):
    MANUAL = "manual"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
