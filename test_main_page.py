from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #Гость открывает главную страницу 
    page = MainPage(browser, link)  
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    
    basket_page = BasketPage(browser, browser.current_url)
    #basket_page.should_be_basket_page()

    #Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty()
    #Ожидаем, что есть текст о том что корзина пуста 
    basket_page.should_be_empty_message()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



