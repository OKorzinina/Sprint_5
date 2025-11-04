from selenium.webdriver.common.by import By

class BasePageLocators:
    """Общие локаторы для всех страниц"""
    LOGO = (By.CSS_SELECTOR, ".react-logo")
    PERSONAL_CABINET_BUTTON = (By.CSS_SELECTOR, "[href='/login']")
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[href='/login'] button")

class MainPageLocators(BasePageLocators):
    """Локаторы главной страницы"""
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")
    HEADER_TITLE = (By.CSS_SELECTOR, "h1")
    BUNS_SECTION = (By.CSS_SELECTOR, "a[href='#buns']")
    SAUCES_SECTION = (By.CSS_SELECTOR, "a[href='#sauces']")
    FILLINGS_SECTION = (By.CSS_SELECTOR, "a[href='#fillings']")

class LoginPageLocators(BasePageLocators):
    """Локаторы страницы входа"""
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Пароль")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")

class RegisterPageLocators(BasePageLocators):
    """Локаторы страницы регистрации"""
    NAME_INPUT = (By.CSS_SELECTOR, "#Имя")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#почта")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#Пароль")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success")

class PersonalCabinetLocators(BasePageLocators):
    """Локаторы личного кабинета"""
    PERSONAL_CABINET_HEADER = (By.CSS_SELECTOR, "h2")
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button")
    PROFILE_SECTION = (By.CSS_SELECTOR, "[href='/profile']")
    ORDERS_SECTION = (By.CSS_SELECTOR, "[href='/orders']")

class ConstructorPageLocators(BasePageLocators):
    """Локаторы страницы конструктора"""
    BUNS_TAB = (By.CSS_SELECTOR, "a[href='#buns']")
    SAUCES_TAB = (By.CSS_SELECTOR, "a[href='#sauces']")
    FILLINGS_TAB = (By.CSS_SELECTOR, "a[href='#fillings']")
    CURRENT_TAB = (By.CSS_SELECTOR, ".tab_tab__1PPdt.tab_tab_type_current__2ZULS")
    INGREDIENT_ITEM = (By.CSS_SELECTOR, ".ingredient")
    BUN_PRICE = (By.CSS_SELECTOR, ".constructor-element__price")

