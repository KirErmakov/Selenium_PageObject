import time

import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('offer', ["offer0", "offer1", "offer2", "offer3", "offer4",
                                   "offer5", "offer6", "offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    time.sleep(1)
    product_page.solve_quiz_and_get_code()
    time.sleep(1)
    product_page.should_be_item_in_basket()
    product_page.should_be_basket_total_equal_item_price()



