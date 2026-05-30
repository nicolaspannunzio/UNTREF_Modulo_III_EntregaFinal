import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def test_caso_1_ordenar_productos(driver):
    # 1. Navegación y login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    # --- LA CURA CONTRA EL FANTASMA DE LA CACHÉ ---
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()

    # 2. Ordenamiento de los elementos (Low to High)
    menu_ordenamiento = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    menu_ordenamiento.select_by_value("lohi")

    elementos_precio = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios_ordenados = []

    for i in elementos_precio:
        numero_puro = float(i.text.replace('$', ''))
        precios_ordenados.append(numero_puro) 
            
    assert precios_ordenados == sorted(precios_ordenados)
    time.sleep(5)


def test_caso_2_carrito(driver):
    # 1. Navegación
    driver.get("https://www.saucedemo.com/")
    
    # --- LA CURA CONTRA EL FANTASMA DE LA CACHÉ ---
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    
    # 2. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    # 3. Agregar todos los elementos del sitio web al carrito
    elementos_carrito = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    time.sleep(3)

    for boton in elementos_carrito:
        boton.click()
    time.sleep(3)

    # 4. Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    # 5. Verificar que todos los elementos estén en el carrito
    elementos_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(elementos_en_carrito) == 6
    time.sleep(3)

    # 6. Ir al checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)

    # 7. Ingresar nombre y clickear "Continue"
    driver.find_element(By.ID, "first-name").send_keys("nicolás")
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)

    # 8. Verificar el error "first name"
    mensaje_validacion = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert mensaje_validacion == "Error: Last Name is required"

    # 9. Ingreso de apellido
    driver.find_element(By.ID, "last-name").send_keys("pannunzio")
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)

    # 10. Verificación "last name"
    mensaje_validacion_apellido = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert mensaje_validacion_apellido == "Error: Postal Code is required"
    time.sleep(3)


def test_caso_3_compra_exitosa(driver):
    # 1. Navegación y login
    driver.get("https://www.saucedemo.com/")

    # --- LA CURA CONTRA EL FANTASMA DE LA CACHÉ ---
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    # 2. Agregar UN elemento al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)

    # 3. Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    # 4. Remover un artículo
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(3)

    # 5. Verificar que el elemento agregado fue eliminado del carrito
    elementos_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(elementos_en_carrito) == 0
    time.sleep(3)

    # 6. Ir a Continue Shopping
    driver.find_element(By.ID, "continue-shopping").click()
    time.sleep(3)

    # Agregar dos elementos al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Volvemos al carrito, paso previo para hacer un assert sin errores
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(3)

    # Verificación de los elementos en el carrito
    elementos_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(elementos_en_carrito) == 2
    time.sleep(3)

    # 7.Click Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)

    # Completar los campos de compra
    driver.find_element(By.ID, "first-name").send_keys("nicolás")
    driver.find_element(By.ID, "last-name").send_keys("pannunzio")
    driver.find_element(By.ID, "postal-code").send_keys("3000")

    time.sleep(3)
    driver.find_element(By.ID, "continue").click()
    
    time.sleep(3)
    driver.find_element(By.ID, "finish").click()

    mensaje_compra = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensaje_compra == "Thank you for your order!" 
    
    time.sleep(5)