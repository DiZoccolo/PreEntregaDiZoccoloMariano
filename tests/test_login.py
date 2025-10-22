from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


#test de login con credenciales correctas
def test_login_correcto(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    test_login_correcto(driver)
    
    #validacion de logeo correcto
    assert "/inventory.html" in driver.current_url