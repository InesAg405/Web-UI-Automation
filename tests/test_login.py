import pytest
from Pages.login_page import LoginPage
from Pages.secure_page import SecurePage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_message()

    secure = SecurePage(driver)
    secure.logout()
    # Use actual title after logout
    assert "The Internet" in driver.title


def test_invalid_username(driver):
    login = LoginPage(driver)
    login.load()
    login.login("wrong", "SuperSecretPassword!")
    assert "Your username is invalid!" in login.get_message()


def test_invalid_password(driver):
    login = LoginPage(driver)
    login.load()
    login.login("tomsmith", "wrongpassword")
    assert "Your password is invalid!" in login.get_message()


@pytest.mark.parametrize("username,password,expected_msg", [
    ("", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "", "Your password is invalid!"),
    ("", "", "Your username is invalid!")
])
def test_empty_fields(driver, username, password, expected_msg):
    login = LoginPage(driver)
    login.load()
    login.login(username, password)
    # Assert based on expected message
    assert expected_msg in login.get_message()