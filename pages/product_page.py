from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()


    def should_be_added_item_in_basket(self):
        added_item = self.browser.find_element(By.XPATH, '//h1')
        item_in_basket = self.browser.find_element(By.XPATH, '//strong[text()="Coders at Work"]')
        assert added_item.text == item_in_basket.text, "Another item is in the basket"
    def should_be_basket_total_equal_item_price(self):
        item_price = self.browser.find_element(By.XPATH, '//p[@class="price_color"]')
        basket_total = self.browser.find_element(By.XPATH, '//strong[text()="£19.99"]')
        assert item_price.text in basket_total.text, "Item price is not equal basket total"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is displayed, but should not"

