import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Username_field, Password_field, Login_button
from data import LOGIN, PASSWORD, MAIN_PAGE

driver = webdriver.Chrome()

def test_login_form():
    driver.get(MAIN_PAGE)

    username_field = driver.find_element(By.CSS_SELECTOR, Username_field).send_keys(LOGIN)

    password_field = driver.find_element(By.ID, Password_field).send_keys(PASSWORD)

    login_button = driver.find_element(By.ID, Login_button).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"