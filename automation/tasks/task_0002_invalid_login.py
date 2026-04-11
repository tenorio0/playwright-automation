from automation.functionalities.login_func import LoginFunc
from playwright_core.testing.base_test import BaseTest


class Task0002InvalidLogin(BaseTest):
    def test_should_show_error_for_locked_out_user(self) -> None:
        login_func = LoginFunc(self.page)

        login_func.login_with_locked_out_user(
            username="locked_out_user",
            password="secret_sauce",
        )
