from automation.functionalities.login_func import LoginFunc
from playwright_core.testing.base_test import BaseTest


class Task0001Login(BaseTest):
    def test_should_login_with_standard_user(self) -> None:
        login_func = LoginFunc(self.page)

        login_func.login_successfully(
            username="standard_user",
            password="secret_sauce",
        )
