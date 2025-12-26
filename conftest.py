import pytest
from drivers.driver_factory import create_driver, quit_driver
from screenshots.screenshot_helper import take_screenshot_on_failure


@pytest.fixture
def driver():
    """
    Provides a WebDriver instance to tests.
    """
    driver = create_driver()
    yield driver
    quit_driver(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshot on test failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name
            take_screenshot_on_failure(driver, test_name)
