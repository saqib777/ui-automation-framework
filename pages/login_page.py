
from selenium.webdriver.common.by import By
from waits.wait_helpers import (
    wait_for_element_visible,
    wait_for_element_clickable
)


class LoginPage:
    """
    Page Object for the Login page.
    """

    URL = "https://the-internet.herokuapp.com/login"

    # Locators
    _username_input = (By.ID, "username")
    _password_input = (By.ID, "password")
    _login_button = (By.CSS_SELECTOR, "button[type='submit']")
    _success_message = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """
        Opens the login page.
        """
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Performs login action using provided credentials.
        """
        username_field = wait_for_element_visible(
            self.driver, self._username_input
        )
        password_field = wait_for_element_visible(
            self.driver, self._password_input
        )

        username_field.clear()
        username_field.send_keys(username)

        password_field.clear()
        password_field.send_keys(password)

        login_btn = wait_for_element_clickable(
            self.driver, self._login_button
        )
        login_btn.click()

    def get_success_message(self):
        """
        Returns the success message text after login.
        """
        message = wait_for_element_visible(
            self.driver, self._success_message
        )
        return message.text
