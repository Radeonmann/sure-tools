from enum import Enum


class PatchApiV1AuthEnableAiResponse200UserUiLayout(str, Enum):
    DASHBOARD = "dashboard"
    INTRO = "intro"

    def __str__(self) -> str:
        return str(self.value)
