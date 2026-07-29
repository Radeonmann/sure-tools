from enum import Enum


class FamilySettingsMoniker(str, Enum):
    FAMILY = "Family"
    GROUP = "Group"

    def __str__(self) -> str:
        return str(self.value)
