from enum import Enum


class PostApiV1AuthSignupResponse201UserUiLayout(str, Enum):
    DASHBOARD = "dashboard"
    INTRO = "intro"

    def __str__(self) -> str:
        return str(self.value)
