from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
def test_about_button():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    burger_menu = driver.find_element(By.CSS_SELECTOR, '[id="react-burger-menu-btn"]').click()

    about_button = driver.find_element(By.CSS_SELECTOR, '[id="about_sidebar_link"]').click()

    assert driver.current_url == 'https://saucelabs.com/'

