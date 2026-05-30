import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # 1. SETUP: Lo que pasa ANTES del caso de prueba
    driver = webdriver.Chrome() # Abre el navegador Chrome
    driver.maximize_window()    # Lo maximiza para evitar bugs de visualización
    
    # 2. LA PAUSA 
    yield driver                # Le pasa el navegador la prueba y se queda esperando
    
    # 3. TEARDOWN: Lo que pasa DESPUÉS del caso de prueba
    driver.quit()               # Cierra la ventana del navegador