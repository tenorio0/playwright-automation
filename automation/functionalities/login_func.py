from playwright.sync_api import Page

from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage


class LoginFunc:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com") -> None:
        self.login_page = LoginPage(page=page, base_url=base_url)
        self.home_page = HomePage(page=page, base_url=base_url)

    def login(self, username: str, password: str) -> None:
        self.login_page.open()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

    def login_successfully(self, username: str, password: str) -> None:
        self.login(username=username, password=password)
        self.home_page.should_be_on_inventory_page()
        self.home_page.should_list_products()

    def login_with_locked_out_user(self, username: str, password: str) -> None:
        self.login(username=username, password=password)
        self.login_page.should_show_error_message(
            "Sorry, this user has been locked out.",
        )
