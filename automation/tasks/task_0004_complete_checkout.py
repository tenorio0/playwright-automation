from automation.functionalities.cart_func import CartFunc
from automation.functionalities.checkout_func import CheckoutFunc
from automation.functionalities.login_func import LoginFunc
from playwright_core.testing.base_test import BaseTest


class Task0004CompleteCheckout(BaseTest):
    def test_should_complete_checkout_with_single_product(self) -> None:
        login_func = LoginFunc(self.page)
        cart_func = CartFunc(self.page)
        checkout_func = CheckoutFunc(self.page)

        login_func.login_successfully(
            username="standard_user",
            password="secret_sauce",
        )
        cart_func.add_product_and_validate_cart(
            product_slug="sauce-labs-backpack",
            product_name="Sauce Labs Backpack",
        )

        checkout_func.complete_checkout(
            product_name="Sauce Labs Backpack",
            first_name="Senior",
            last_name="QA",
            postal_code="12345",
        )
