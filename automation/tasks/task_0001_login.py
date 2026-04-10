from automation.functionalities.login_func import LoginFunc
from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage
from core.testing.base_test import BaseTest


class Task0001Login(BaseTest):
    def test_should_login_with_standard_user(self) -> None:
        base_url = "https://www.saucedemo.com"
        login_page = LoginPage(page=self.page, base_url=base_url)
        home_page = HomePage(page=self.page, base_url=base_url)
        login_func = LoginFunc(login_page=login_page, home_page=home_page)

        login_func.realizar_login_com_sucesso(
            username="standard_user",
            password="secret_sauce",
        )
