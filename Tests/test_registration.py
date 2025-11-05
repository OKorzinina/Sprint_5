from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPage:

    def test_successful_registration(self, browser_driver):
        """Тест успешной регистрации пользователя"""
        browser = browser_driver
        browser.get(URLS.REG_PAGE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        browser.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        browser.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        browser.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        browser.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        login_button_visible = browser.find_element(*AuthPageLocators.login_account_btn).is_displayed()

        assert browser.current_url == URLS.AUTH_PAGE_URL and login_button_visible


    def test_registration_short_password_error(self, browser_driver):
        """Тест регистрации с коротким паролем (проверка ошибки)"""
        browser = browser_driver
        browser.get(URLS.REG_PAGE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        browser.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        browser.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        browser.find_element(*RegistrationPageLocators.password_input).send_keys(12345)
        browser.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(browser, 3).until(EC.visibility_of_any_elements_located(RegistrationPageLocators.error_message_incorrect_password))
        error_message = browser.find_element(*RegistrationPageLocators.error_message_incorrect_password).text

        assert (error_message == 'Некорректный пароль') and (browser.current_url == URLS.REG_PAGE_URL)


    def test_duplicate_registration_error(self, browser_driver):
        """Тест повторной регистрации (проверка ошибки)"""
        browser = browser_driver
        browser.get(URLS.REG_PAGE_URL)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        browser.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        browser.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        browser.find_element(*RegistrationPageLocators.password_input).send_keys(Person.password)
        browser.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(RegistrationPageLocators.error_message_double_reg))   
        error_message = browser.find_element(*RegistrationPageLocators.error_message_double_reg).text

        assert (error_message == 'Такой пользователь уже существует') and (browser.current_url == URLS.REG_PAGE_URL)


