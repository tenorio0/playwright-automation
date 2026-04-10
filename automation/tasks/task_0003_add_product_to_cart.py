from automation.functionalities.cart_func import CartFunc
from automation.functionalities.login_func import LoginFunc
from automation.pages.cart_page import CartPage
from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage
from core.testing.base_test import BaseTest


class Task0003AddProductToCart(BaseTest):
    def test_should_add_backpack_to_cart(self) -> None:
        base_url = "https://www.saucedemo.com"
        login_page = LoginPage(page=self.page, base_url=base_url)
        home_page = HomePage(page=self.page, base_url=base_url)
        cart_page = CartPage(page=self.page, base_url=base_url)
        login_func = LoginFunc(login_page=login_page, home_page=home_page)
        cart_func = CartFunc(home_page=home_page, cart_page=cart_page)

        login_func.realizar_login_com_sucesso(
            username="standard_user",
            password="secret_sauce",
        )
        cart_func.adicionar_produto_e_validar_carrinho(
            product_slug="sauce-labs-backpack",
            product_name="Sauce Labs Backpack",
        )
