import pytest
from drivers.driver_factory import create_driver, quit_driver


@pytest.fixture
def driver():
    """
    Pytest fixture to provide a WebDriver instance to tests.
    Handles setup and teardown automatically.
    """
    driver = create_driver()
    yield driver
    quit_driver(driver)

