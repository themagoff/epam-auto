from selenium.webdriver.common.by import By
from task07.pages.base_page import BasePage


class AuthPage(BasePage):
    _url = 'https://esia-portal1.test.gosuslugi.ru/'
    _login_input = (By.ID, 'login')
    _pwd_input = (By.ID, 'password')
    _not_remember_checkbox = (By.XPATH, "//label[@for='ufoPC']")
    _enter_button = (By.ID, 'loginByPwdButton')

    def fill_login_input(self, login):
        self.get_element(*self._login_input).send_keys(login)

    def fill_pwd_input(self, pwd):
        self.get_element(*self._pwd_input).send_keys(pwd)

    def click_enter_btn(self):
        self.get_element(*self._enter_button).click()

    def should_be_err_msg_incorrect_login(self):
        assert self.text_is_displayed("Введите телефон, почту или СНИЛС"), "Error message is not displayed"

    def should_be_err_msg_incorrect_pwd(self):
        assert self.text_is_displayed("Введен неверный логин или пароль"), "Error message is not displayed"

    def should_be_profile_page_open(self):
        assert self.current_url == 'https://esia-portal1.test.gosuslugi.ru/profile/user/personal'
