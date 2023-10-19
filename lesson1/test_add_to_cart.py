from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    text_before = driver.find_element(By.CSS_SELECTOR, '[id=item_0_title_link]>[class="inventory_item_name "]').text

    adding_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]').click()

    cart = driver.find_element(By.CSS_SELECTOR, '[class = "shopping_cart_link"]').click()

    text_after = driver.find_element(By.CSS_SELECTOR, '[id=item_0_title_link]>[class=inventory_item_name]').text
    assert text_after == text_before
