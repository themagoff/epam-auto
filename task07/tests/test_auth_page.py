from task07.pages.auth_page import AuthPage
from task07.pages.profile_page import ProfilePage


def test_incorrect_login(driver):
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('incorrect_login')
    page.fill_pwd_input('some_pwd')
    page.click_enter_btn()
    page.should_be_err_msg_incorrect_login()


def test_incorrect_pwd(driver):
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('test@test.com')
    page.fill_pwd_input('some_pwd')
    page.click_enter_btn()
    page.should_be_err_msg_incorrect_pwd()


def test_correct_login_and_pwd(driver):
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('')
    page.fill_pwd_input('')
    page.click_enter_btn()
    profile_page = ProfilePage(driver)
    profile_page.should_be_profile_page_url()
