from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
import time
from selenium.webdriver.common.by import By
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):#, offer):
    #link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
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


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 

    #Открываем страницу товара 
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  
    product_page = ProductPage(browser, browser.current_url)
    #product_page.should_be_add_to_basket_btn()

    #Добавляем товар в корзину 
    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser): 
    #Открываем страницу товара 
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  
    product_page = ProductPage(browser, browser.current_url)
    
    #product_page.should_be_add_to_basket_btn()

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  
    product_page = ProductPage(browser, browser.current_url)
    
    #product_page.should_be_add_to_basket_btn()
    
    #Добавляем товар в корзину
    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



