from selenium import webdriver
from selenium.webdriver.common.by import By
# from test_login import test_login_correcto as tlc
import pytest

driver = webdriver.Chrome()
driver.implicitly_wait(5)
print("catalogo")

def test_elementos_ui(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    #validacion de titulo
    assert "Swag Labs" in driver.title

    #validacion de elementos importantes de interfaz
    menu = driver.find_elements(By.ID, "react-burger-menu-btn")
    filter = driver.find_elements(By.CLASS_NAME, "product_sort_container")
    footer = driver.find_elements(By.CLASS_NAME, "footer")

    assert menu and menu[0].is_displayed(), "el menu no es visible"
    assert filter and filter[0].is_displayed(), "el filtro no es visible"
    assert footer and footer[0].is_displayed(), "el footer no es visible"

    #verificacion de existencia de productos
    try:
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No existen productos visibles en la pagina"
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise