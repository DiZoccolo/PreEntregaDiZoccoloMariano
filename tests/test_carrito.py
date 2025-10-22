from selenium import webdriver
from selenium.webdriver.common.by import By
from test_login import test_login_correcto as tlc
import pytest

driver = webdriver.Chrome()
driver.implicitly_wait(5)
print("carrito")
def test_agregar_producto_carrito(driver):
    tlc(driver)

    #validacion de actualizacion de carrito de compra
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    productos[0].find_element(By.TAG_NAME, "button").click()

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link").text
    assert carrito == "1"

    #navegacion y comprobacion de adicion de producto al carrito de compras
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.CLASS_NAME, "cart_list")
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link").text
    assert cart == "1"