from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

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
        assert self.is_element_present(By.CSS_SELECTOR, "#messages strong"), "Messages are not presented"
        elements = self.browser.find_elements(By.CSS_SELECTOR, "#messages strong")
        assert elements[0].text == name, "Different name of product"
        assert True

    def should_be_the_same_price_of_product(self, price):
        assert self.is_element_present(By.CSS_SELECTOR, "#messages strong"), "Messages are not presented"
        elements = self.browser.find_elements(By.CSS_SELECTOR, "#messages strong")
        assert elements[2].text == price, "Different price of product"
        assert True
