from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # открыть страницу товара
    # добавить в корзину
    # получить сообщение об успешном добавлении
    # проверить, что название совпадает
    # проверить, что цена совпадает
    product_page = ProductPage(browser, link)
    product_page.open()
    
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()

    product_page.should_be_add_to_basket_btn()
    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    product_page.should_be_the_same_name_of_product(product_name)
    product_page.should_be_the_same_price_of_product(product_price)


@pytest.mark.xfail  # так как сообщение об успехе есть
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    #Открываем страницу товара 
    product_page = ProductPage(browser, link)
    product_page.open()
    
    #Добавляем товар в корзину 
    product_page.should_be_add_to_basket_btn()
    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    #Открываем страницу товара 
    product_page = ProductPage(browser, link)
    product_page.open()

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.xfail() # так как сообщение есть
def test_message_disappeared_after_adding_product_to_basket(browser): 
    #Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    
    #Добавляем товар в корзину
    product_page.should_be_add_to_basket_btn()
    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Гость открывает главную страницу 
    page = ProductPage(browser, link)
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()    
    basket_page = BasketPage(browser, browser.current_url)

    #Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty()
    #Ожидаем, что есть текст о том что корзина пуста 
    basket_page.should_be_empty_message()



@pytest.mark.users_tests
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #открыть страницу регистрации
        self.page = MainPage(browser, link)  
        self.page.open()  
        self.page.go_to_login_page()

        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

        #зарегистрировать нового пользователя;
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "pwd"
        self.login_page.register_new_user(email=email, password=password)

        #проверить, что пользователь залогинен.
        self.page.should_be_authorized_user()



    def test_user_cant_see_success_message(self,  browser):     
        #Открываем страницу товара 
        self.product_page = ProductPage(browser, link)
        self.product_page.open()

        #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # открыть страницу товара
        # добавить в корзину
        # получить сообщение об успешном добавлении
        # проверить, что название совпадает
        # проверить, что цена совпадает
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        
        product_name = self.product_page.get_product_name()
        product_price = self.product_page.get_product_price()

        self.product_page.should_be_add_to_basket_btn()
        button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()

        self.product_page.should_be_the_same_name_of_product(product_name)
        self.product_page.should_be_the_same_price_of_product(product_price)


