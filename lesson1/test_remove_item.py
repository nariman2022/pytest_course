from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.
driver =  webdriver.Chrome()

def test_remove_item():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    adding_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]').click()

    remove_from_cart = driver.find_element(By.XPATH, '//button [@data-test="remove-sauce-labs-bike-light"]').click()

    cart_after = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')




