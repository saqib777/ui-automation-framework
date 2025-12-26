
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def create_driver():
    """
    Creates and returns a configured Chrome WebDriver instance.
    """
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    return driver


def quit_driver(driver):
    """
    Safely quits the WebDriver instance.
    """
    if driver:
        driver.quit()

