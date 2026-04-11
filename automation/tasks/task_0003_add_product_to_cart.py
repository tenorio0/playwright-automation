from automation.functionalities.cart_func import CartFunc
from automation.functionalities.login_func import LoginFunc
from playwright_core.testing.base_test import BaseTest


class Task0003AddProductToCart(BaseTest):
    def test_should_add_backpack_to_cart(self) -> None:
        login_func = LoginFunc(self.page)
        cart_func = CartFunc(self.page)

        login_func.login_successfully(
            username="standard_user",
            password="secret_sauce",
        )
        cart_func.add_product_and_validate_cart(
            product_slug="sauce-labs-backpack",
            product_name="Sauce Labs Backpack",
        )
