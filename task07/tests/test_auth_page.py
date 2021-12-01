from task07.pages.auth_page import AuthPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_incorrect_login():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('incorrect_login')
    page.fill_pwd_input('some_pwd')
    page.click_enter_btn()
    page.should_be_err_msg_incorrect_login()


def test_incorrect_pwd():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('test@test.com')
    page.fill_pwd_input('some_pwd')
    page.click_enter_btn()
    page.should_be_err_msg_incorrect_pwd()


def test_correct_login_and_pwd():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    page = AuthPage(driver)
    page.open()
    page.fill_login_input('test@test.com')
    page.fill_pwd_input('correct_pwd')
    page.click_enter_btn()
    page.should_be_profile_page_open()
