from pages.login_page import LoginPage


def test_valid_login(driver):
    """
    Verify that a user can log in with valid credentials.
    """
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        username="tomsmith",
        password="SuperSecretPassword!"
    )

    success_message = login_page.get_success_message()

    assert "You logged into a secure area!" in success_message
