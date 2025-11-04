from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileNavigation:

    def test_profile_button_redirects_to_profile_page(self, driver, get_login_driver):
        """Verify successful redirection to the profile page upon clicking 'Profile' button on main page."""
        browser_instance = get_login_driver
        wait = WebDriverWait(browser_instance, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        browser_instance.find_element(*MainPageLocators.personal_account_btn).click()
        wait.until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        is_save_button_present = browser_instance.find_element(*PersonalAreaLocators.save_btn).is_displayed()

        assert browser_instance.current_url == URLS.PROFILE_PAGE_URL and is_save_button_present


    def test_constructor_button_navigates_to_main_page_from_profile(self, driver, get_login_driver):
        """Ensure navigation from personal profile to ingredient constructor page using the 'Constructor' button."""
        browser_instance = get_login_driver
        wait = WebDriverWait(browser_instance, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        browser_instance.find_element(*MainPageLocators.personal_account_btn).click()
        wait.until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        browser_instance.find_element(*PersonalAreaLocators.constructor_btn).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.bun))
        is_bun_visible = browser_instance.find_element(*MainPageLocators.bun).is_displayed()

        assert browser_instance.current_url == URLS.MAIN_PAGE_URL and is_bun_visible

    def test_logo_click_redirects_to_constructor_page(self, driver, get_login_driver):
        """Validate return to the ingredient constructor after clicking the logo while in personal profile."""
        browser_instance = get_login_driver
        wait = WebDriverWait(browser_instance, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        browser_instance.find_element(*MainPageLocators.personal_account_btn).click()
        wait.until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        browser_instance.find_element(*PersonalAreaLocators.logo_btn).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.bun))
        is_bun_displayed = browser_instance.find_element(*MainPageLocators.bun).is_displayed()

        assert browser_instance.current_url == URLS.MAIN_PAGE_URL and is_bun_displayed

    def test_logout_button_redirects_to_login_page(self, driver, get_login_driver):
        """Confirm redirection to login page after logging out from personal profile using the 'Logout' button."""
        browser_instance = get_login_driver
        wait = WebDriverWait(browser_instance, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        browser_instance.find_element(*MainPageLocators.personal_account_btn).click()
        wait.until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        browser_instance.find_element(*PersonalAreaLocators.exit_btn).click()
        wait.until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        is_login_button_visible = browser_instance.find_element(*AuthPageLocators.login_account_btn).is_displayed()

        assert browser_instance.current_url == URLS.AUTH_PAGE_URL and is_login_button_visible



    
