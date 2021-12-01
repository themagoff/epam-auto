from selenium.webdriver.common.by import By
from task07.pages.base_page import BasePage


class ProfilePage(BasePage):
    _url = 'https://esia-portal1.test.gosuslugi.ru/profile/user/personal'
    _logout_button = (By.CLASS_NAME, '.link-logout')

    def logout(self):
        self._driver.get_element(*self._logout_button).click()
