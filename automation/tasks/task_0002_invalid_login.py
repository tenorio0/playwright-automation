from automation.functionalities.login_func import LoginFunc
from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage
from core.testing.base_test import BaseTest


class Task0002InvalidLogin(BaseTest):
    def test_should_show_error_for_locked_out_user(self) -> None:
        base_url = "https://www.saucedemo.com"
        login_page = LoginPage(page=self.page, base_url=base_url)
        home_page = HomePage(page=self.page, base_url=base_url)
        login_func = LoginFunc(login_page=login_page, home_page=home_page)

        login_func.realizar_login_com_usuario_bloqueado(
            username="locked_out_user",
            password="secret_sauce",
        )
