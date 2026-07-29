from enum import Enum


class PostApiV1AuthSsoCreateAccountResponse200UserUiLayout(str, Enum):
    DASHBOARD = "dashboard"
    INTRO = "intro"

    def __str__(self) -> str:
        return str(self.value)
