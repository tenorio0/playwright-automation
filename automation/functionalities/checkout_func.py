from playwright.sync_api import Page

from automation.pages.cart_page import CartPage
from automation.pages.checkout_complete_page import CheckoutCompletePage
from automation.pages.checkout_information_page import CheckoutInformationPage
from automation.pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutFunc:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com") -> None:
        self.cart_page = CartPage(page=page, base_url=base_url)
        self.checkout_information_page = CheckoutInformationPage(page=page, base_url=base_url)
        self.checkout_overview_page = CheckoutOverviewPage(page=page, base_url=base_url)
        self.checkout_complete_page = CheckoutCompletePage(page=page, base_url=base_url)

    def complete_checkout(
        self,
        product_name: str,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        self.cart_page.click_checkout()
        self.checkout_information_page.should_be_on_checkout_information_page()
        self.checkout_information_page.fill_first_name(first_name)
        self.checkout_information_page.fill_last_name(last_name)
        self.checkout_information_page.fill_postal_code(postal_code)
        self.checkout_information_page.continue_checkout()
        self.checkout_overview_page.should_be_on_checkout_overview_page()
        self.checkout_overview_page.should_contain_product(product_name)
        self.checkout_overview_page.click_finish()
        self.checkout_complete_page.should_show_order_success()
