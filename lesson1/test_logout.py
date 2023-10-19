from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_logout():
    driver.get("https://www.saucedemo.com/")

    before_test = driver.find_element(By.CSS_SELECTOR, '[class = login_logo]').text
    url_before = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(2)

    logout_button = driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link")
    logout_button.click()

    after_test = driver.find_element(By.CSS_SELECTOR, '[class = login_logo]').text
    assert before_test == after_test

    url_after = driver.current_url
    assert url_before == url_after

    driver.quit()