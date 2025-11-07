from locators import MainPageLocators
from urls import URLS
from selenium import webdriver

class TestBurgerConstructorPage:
    def test_go_to_buns_section(self, browser):
        """Тест перехода в раздел Булки"""
        browser.get(URLS.MAIN_PAGE_URL)
        browser.find_element(*MainPageLocators.sauces_btn).click()
        browser.find_element(*MainPageLocators.bun_btn).click()
        bun_header = browser.find_element(*MainPageLocators.bun).text
        buns_visible = browser.find_element(*MainPageLocators.bun_ul).is_displayed()

        assert bun_header == 'Булки' and buns_visible


    def test_go_to_sauces_section(self, browser):
        """Тест перехода в раздел Соусы"""
        browser.get(URLS.MAIN_PAGE_URL)
        browser.find_element(*MainPageLocators.sauces_btn).click()
        sauce_header = browser.find_element(*MainPageLocators.sauces).text
        sauces_visible = browser.find_element(*MainPageLocators.sauces_ul).is_displayed()

        assert sauce_header == 'Соусы' and sauces_visible


    def test_go_to_fillings_section(self, browser):
        """Тест перехода в раздел Начинки"""
        browser.get(URLS.MAIN_PAGE_URL)
        browser.find_element(*MainPageLocators.toppings_btn).click()
        filling_header = browser.find_element(*MainPageLocators.topping).text
        fillings_visible = browser.find_element(*MainPageLocators.topping_ul).is_displayed()

        assert filling_header == 'Начинки' and fillings_visible
