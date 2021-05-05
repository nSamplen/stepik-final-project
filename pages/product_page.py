from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    
    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name_element.text

    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price_element.text

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "'Add to basket' button is not presented"
        assert True

    def should_be_the_same_name_of_product(self, name):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_INFO), "Messages are not presented"
        elements = self.browser.find_elements(*ProductPageLocators.ADDED_PRODUCT_INFO)
        assert elements[0].text == name, "Different name of product"
        assert True

    def should_be_the_same_price_of_product(self, price):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_INFO), "Messages are not presented"
        elements = self.browser.find_elements(*ProductPageLocators.ADDED_PRODUCT_INFO)
        assert elements[2].text == price, "Different price of product"
        assert True
