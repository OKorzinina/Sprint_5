from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileNavigation:

    def test_profile_link_navigates_to_profile_page(self, driver, get_login_driver):
        """Verify navigation to the profile page from the main page using the 'Profile' button."""
        browser = get_login_driver
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(MainPageLocators.personal_account_btn))
        browser.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        submit_changes_visible = browser.find_element(*PersonalAreaLocators.save_btn).is_displayed()

        assert browser.current_url == URLS.PROFILE_PAGE_URL and submit_changes_visible

    def test_logo_redirects_to_main_page_from_profile(self, driver, get_login_driver):
        """Verify redirection to the constructor page from the profile section via logo click."""
        browser = get_login_driver
        wait = WebDriverWait(browser, 10)
        wait.until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        browser.find_element(*MainPageLocators.personal_account_btn).click()
        wait.until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        browser.find_element(*PersonalAreaLocators.logo_btn).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.bun))
        is_bun_visible = browser.find_element(*MainPageLocators.bun).is_displayed()

        assert browser.current_url == URLS.MAIN_PAGE_URL and is_bun_visible

