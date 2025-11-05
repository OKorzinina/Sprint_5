from selenium import webdriver
import pytest
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from data import Person


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()



@pytest.fixture
def get_login_driver(browser):
    browser.get(URLS.MAIN_PAGE_URL)
    browser.find_element(*MainPageLocators.personal_account_btn).click()
    browser.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
    browser.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
    browser.find_element(*AuthPageLocators.login_account_btn).click()

    return browser

   
