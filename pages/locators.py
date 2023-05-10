from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]')
    ITEM_TO_BUY = (By.XPATH, '//h2[@class="col-sm-6 h3"]')





