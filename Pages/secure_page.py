# pages/secure_page.py
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class SecurePage(BasePage):
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button")

    def logout(self):
        self.click(self.LOGOUT_BTN)