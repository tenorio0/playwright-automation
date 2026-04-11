from playwright.sync_api import Page

from automation.pages.cart_page import CartPage
from automation.pages.home_page import HomePage


class CartFunc:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com") -> None:
        self.home_page = HomePage(page=page, base_url=base_url)
        self.cart_page = CartPage(page=page, base_url=base_url)

    def add_product_to_cart(self, product_slug: str) -> None:
        self.home_page.add_product_to_cart(product_slug)

    def open_cart(self) -> None:
        self.home_page.open_cart()

    def add_product_and_validate_cart(
        self,
        product_slug: str,
        product_name: str,
        quantity: int = 1,
    ) -> None:
        self.add_product_to_cart(product_slug)
        self.home_page.should_have_cart_badge(quantity)
        self.open_cart()
        self.cart_page.should_be_on_cart_page()
        self.cart_page.should_contain_product(product_name)
