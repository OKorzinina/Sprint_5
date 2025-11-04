from data import Person
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    def test_login_in_personal_account_btn_success(self, driver): #Вход через кнопку Личный кабинет
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_login_btn_success(self, driver): #Вход через кнопку Войти в аккаунт
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


     def test_login_in_registration_form_success(self, driver): #Вход через форму регистрации
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


    def test_login_in_recover_form_success(self, driver): #Вход через форму восстановления
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.place_order_button))
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')


from data import Person
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    def test_login_from_main_login_button(self, driver):
        """Авторизация через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)

        driver.find_element(*MainPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_text = driver.find_element(*MainPageLocators.place_order_button).text

        assert driver.current_url == URLS.MAIN_PAGE_URL and order_text == 'Оформить заказ'

    def test_login_from_personal_account_button(self, driver):
        """Авторизация через кнопку 'Личный кабинет' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)

        driver.find_element(*MainPageLocators.personal_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.place_order_button)
        )
        order_text = driver.find_element(*MainPageLocators.place_order_button).text

        assert driver.current_url == URLS.MAIN_PAGE_URL and order_text == 'Оформить заказ'

    def test_login_from_registration_page(self, driver):
        """Авторизация из формы регистрации"""
        driver.get(URLS.REG_PAGE_URL)

        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_text = driver.find_element(*MainPageLocators.place_order_button).text

        assert driver.current_url == URLS.MAIN_PAGE_URL and order_text == 'Оформить заказ'

    def test_login_from_recover_page(self, driver):
        """Авторизация через форму восстановления пароля"""
        driver.get(URLS.RECOVER_PAGE_URL)

        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )
        order_text = driver.find_element(*MainPageLocators.place_order_button).text

        assert driver.current_url == URLS.MAIN_PAGE_URL and order_text == 'Оформить заказ'


