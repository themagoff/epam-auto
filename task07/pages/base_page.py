from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class BasePage:
    _url = None

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self._url)

    def get_element(self, selector_type, selector, timeout=5):
        return WebDriverWait(self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((selector_type, selector))
        )

    def get_elements(self, selector_type, selector, timeout=5):
        return WebDriverWait(self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_any_elements_located((selector_type, selector))
        )

    def text_is_displayed(self, text, timeout=10):
        try:
            WebDriverWait(self._driver, timeout=timeout).until(
                expected_conditions.visibility_of_element_located((By.XPATH, ".//*[contains(text(),'" + text + "')]"))
            )
        except TimeoutException:
            return False
        return True
