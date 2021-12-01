import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://esia-portal1.test.gosuslugi.ru/")

time.sleep(5)

driver.find_elements(By.XPATH, "//input")
driver.find_element(By.XPATH, "//*[@id='login']").send_keys("test_login")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("test_pass")
driver.find_element(By.XPATH, "//label[@for='ufoPC']").click()

time.sleep(5)
