from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()


    def should_be_item_in_basket(self):
        item_in_basket = self.browser.find_element(By.XPATH, '//div[@class="alertinner "]')
        added_item = self.browser.find_element(By.XPATH, '//h1')
        assert added_item.text in item_in_basket.text, "Such item is not added"

    def should_be_basket_total_equal_item_price(self):
        item_price = self.browser.find_elements(By.XPATH, '//p[@class="price_color"]')[0]
        basket_total = self.browser.find_element(By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]')
        assert item_price.text == basket_total.text, "Values are not equal"
