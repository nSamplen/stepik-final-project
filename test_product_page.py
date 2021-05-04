from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import time
from selenium.webdriver.common.by import By
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_add_to_basket_btn()

    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()

    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    product_page.solve_quiz_and_get_code()

    #time.sleep(1)

    product_page.should_be_the_same_name_of_product(product_name)
    product_page.should_be_the_same_price_of_product(product_price)

    #time.sleep(200)



