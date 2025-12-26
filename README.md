# UI Automation Framework (SDET-Style)

## Overview

This repository contains a scalable UI automation framework built using Python, Selenium, and Pytest, following clean architecture principles and the Page Object Model (POM).

The framework is designed with an **SDET mindset**, focusing not just on test execution, but on maintainability, debuggability, and long-term scalability. Every layer has a clear responsibility, and test code remains free from low-level automation noise.

This project is intended as both a learning reference and a portfolio-quality demonstration of real-world automation practices.

---

## Key Goals of This Framework

- Keep test code clean and readable  
- Isolate Selenium logic from test scenarios  
- Handle waits, retries, logging, and screenshots centrally  
- Support easy scaling as test coverage grows  
- Be CI-friendly and production-ready  

This is not a collection of recorded scripts.  
It is a deliberately structured automation framework.

---

## Tech Stack

- **Language:** Python  
- **UI Automation:** Selenium WebDriver  
- **Test Runner:** Pytest  
- **Design Pattern:** Page Object Model (POM)  

---

## Project Structure

```
ui-automation-framework/
│
├── tests/
│ └── test_login.py
│
├── pages/
│ └── login_page.py
│
├── drivers/
│ └── driver_factory.py
│
├── waits/
│ └── wait_helpers.py
│
├── screenshots/
│ └── screenshot_helper.py
│
├── assertions/
│ └── custom_assertions.py
│
├── logging/
│ └── logger_helper.py
│
├── data/
│ └── test_data_generator.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

```


Each folder represents a single responsibility and is designed to evolve independently.

---

## Framework Architecture (High-Level)

### Tests Layer
Contains only test scenarios.
- No Selenium calls
- No locators
- No waits
- No setup or teardown logic

Tests describe **what** is being validated, not **how**.

---

### Pages Layer
Implements the Page Object Model.
- Stores locators
- Encapsulates UI interactions
- Uses wait helpers internally

Each page represents a real application screen.

---

### Drivers Layer
Responsible for browser lifecycle.
- Driver creation
- Browser configuration
- Safe teardown

Tests never interact with WebDriver setup directly.

---

### Utilities Layer
Shared automation utilities used across the framework:
- Explicit waits
- Retry logic
- Screenshot capture
- Custom assertions
- Logging
- Test data generation

This layer keeps test and page code clean and consistent.

---

## Example Test (Happy Path Login)

def test_valid_login(driver):
login_page = LoginPage(driver)
login_page.open()
login_page.login(
    username="tomsmith",
    password="SuperSecretPassword!"
)

success_message = login_page.get_success_message()
assert "You logged into a secure area!" in success_message


This test reads like a scenario, not automation code.

---

## Screenshot on Failure

The framework automatically captures screenshots when a test fails using Pytest hooks.

- No manual calls inside tests
- Screenshots are timestamped
- Test name is included in the filename

This is especially useful in CI environments where visual debugging is critical.

---

## How to Run Tests

1. Install dependencies:

