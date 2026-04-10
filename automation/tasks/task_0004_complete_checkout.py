from automation.functionalities.cart_func import CartFunc
from automation.functionalities.checkout_func import CheckoutFunc
from automation.functionalities.login_func import LoginFunc
from automation.pages.cart_page import CartPage
from automation.pages.checkout_complete_page import CheckoutCompletePage
from automation.pages.checkout_information_page import CheckoutInformationPage
from automation.pages.checkout_overview_page import CheckoutOverviewPage
from automation.pages.home_page import HomePage
from automation.pages.login_page import LoginPage
from playwright_core.testing.base_test import BaseTest


class Task0004CompleteCheckout(BaseTest):
    def test_should_complete_checkout_with_single_product(self) -> None:
        base_url = "https://www.saucedemo.com"
        login_page = LoginPage(page=self.page, base_url=base_url)
        home_page = HomePage(page=self.page, base_url=base_url)
        cart_page = CartPage(page=self.page, base_url=base_url)
        checkout_information_page = CheckoutInformationPage(page=self.page, base_url=base_url)
        checkout_overview_page = CheckoutOverviewPage(page=self.page, base_url=base_url)
        checkout_complete_page = CheckoutCompletePage(page=self.page, base_url=base_url)

        login_func = LoginFunc(login_page=login_page, home_page=home_page)
        cart_func = CartFunc(home_page=home_page, cart_page=cart_page)
        checkout_func = CheckoutFunc(
            cart_page=cart_page,
            checkout_information_page=checkout_information_page,
            checkout_overview_page=checkout_overview_page,
            checkout_complete_page=checkout_complete_page,
        )

        login_func.realizar_login_com_sucesso(
            username="standard_user",
            password="secret_sauce",
        )
        cart_func.adicionar_produto_e_validar_carrinho(
            product_slug="sauce-labs-backpack",
            product_name="Sauce Labs Backpack",
        )

        checkout_func.complete_checkout(
            product_name="Sauce Labs Backpack",
            first_name="Senior",
            last_name="QA",
            postal_code="12345",
        )
