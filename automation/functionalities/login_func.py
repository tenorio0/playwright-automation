from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage


class LoginFunc:
    def __init__(self, login_page: LoginPage, home_page: HomePage) -> None:
        self.login_page = login_page
        self.home_page = home_page

    def realizar_login(self, username: str, password: str) -> None:
        self.login_page.open()
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login()

    def realizar_login_com_sucesso(self, username: str, password: str) -> None:
        self.realizar_login(username=username, password=password)
        self.home_page.should_be_on_inventory_page()
        self.home_page.should_list_products()

    def realizar_login_com_usuario_bloqueado(self, username: str, password: str) -> None:
        self.realizar_login(username=username, password=password)
        self.login_page.should_show_error_message(
            "Sorry, this user has been locked out.",
        )
