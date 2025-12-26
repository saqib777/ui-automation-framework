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
