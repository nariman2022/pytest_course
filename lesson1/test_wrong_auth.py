from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME_FIELD = '//input[@data-test="username"]'
PASSWORD_FIELD = '//input[@data-test="password"]'
LOGIN_BUTTON = '//input[@data-test="login-button"]'

def test_wrong_auth():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, USERNAME_FIELD).send_keys('error_user')

    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys("error_user")

    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    fail_message = driver.find_element(By.XPATH, "//div[@class = 'error-message-container error']")
    assert fail_message.text == 'Epic sadface: Username and password do not match any user in this service'

