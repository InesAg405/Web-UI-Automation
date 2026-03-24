# Web UI Automation Framework

Automated functional testing of web applications using **Python 3**, **Selenium **, and **Pytest**, implementing the **Page Object Model (POM)** with HTML reports.

---

## Features

- Login page tests (positive, negative, edge cases)  
- Secure area tests (logout)  
- Parameterized tests with multiple data sets  
- Pytest fixture for browser setup and teardown  
- HTML report generation for test results  
- Scalable Page Object Model structure  

---

## Project Structure
├── pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── login_page.py
│ └── secure_page.py
├── tests/ # Test cases
│ ├── test_login.py
│ └── test_secure_area.py
├── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── reports/ # HTML reports (auto-generated)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## How It Works
Page Object Model (POM): separates test logic from UI interactions
Pages: define element locators and user actions (login, logout, etc.)
Fixtures: manage browser setup and teardown automatically
Pytest: discovers test files, runs parametrized tests, handles assertions
HTML Reports: visually shows which tests passed or failed

