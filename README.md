# 🚀 Trabajo Final Integrador - Módulo 3

Este repositorio contiene las resoluciones correspondientes al Trabajo Final Integrador del Módulo 3 de la **Diplomatura en Control de Calidad de Software** dictada por la UNTREF.

El proyecto combina el desarrollo de algoritmos lógicos en Python, control de flujos, manejo de excepciones y la arquitectura de pruebas automatizadas.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Cypress](https://img.shields.io/badge/Cypress-17202C?style=for-the-badge&logo=cypress&logoColor=white)
![QA Automation](https://img.shields.io/badge/QA_Automation-239120?style=for-the-badge&logo=testing-library&logoColor=white)

## 🎯 Estructura y Detalle del Proyecto

El trabajo está estructurado en tres programas principales independientes, diseñados bajo buenas prácticas de modularización y robustez:

* **`punto1.py` (Validación de Números Primos):** Algoritmo matemático para la detección y validación de números primos. Cuenta con manejo de excepciones para inputs inválidos.
* **`punto2.py` (Ecuaciones Cuadráticas):** Calculadora de raíces cuadradas utilizando la fórmula de Bhaskara, también conocida como fórmula resolvente. Implementa modularización mediante funciones, evaluación de casos límite (división por cero) y cálculo de discriminante.
* **`punto3` (Suite de Pruebas Automatizadas E2E y API):** Framework de automatización construido con Python, Pytest y Selenium WebDriver. 
* **Testing Web (SauceDemo):** Cobertura de flujos End-to-End (Happy Paths y Testing Negativo), validación dinámica del DOM, manejo de esperas (Timeouts), aislamiento de estado (limpieza de caché/Local Storage).
* **Reporting:** Generación automática de reportes de ejecución interactivos en HTML mediante `pytest-html`.
* **Testing de API (PokeAPI):** Construido con JavaScript, Node.js y Cypress. Ejecución de peticiones HTTP (GET), parseo de respuestas JSON y validación estricta de variables de estado y parámetros.
* **`TFI-M3-UNTREF-INFORME_NicolasPannunzio.pdf` - Informe Técnico:** Documentación formal voluntaria que detalla paso a paso la arquitectura del entorno híbrido, análisis del DOM, justificación de localizadores, manejo de excepciones y las conclusiones del proyecto.


## 💻 Instrucciones de Ejecución

Para probar tanto los scripts lógicos como las suites de automatización en tu entorno local, seguí estos pasos:

### 1. Clonar el repositorio y acceder 
```bash
 git clone [https://github.com/nicolaspannunzio/UNTREF_Modulo_III_EntregaFinal.git](https://github.com/nicolaspannunzio/UNTREF_Modulo_III_EntregaFinal.git) 
 cd UNTREF_Modulo_III_EntregaFinal

# Activar el entorno virtual (en Windows)
.\venv\Scripts\activate

# Instalar dependencias del proyecto
pip install -r requirements.txt

# Ejecutar scripts lógicos locales
python punto1.py
python punto2.py

# Ejecutar la suite de pruebas web y generar el reporte HTML
pytest
 
 # Instalar los módulos de Node necesarios (node_modules)
npm install

# Abrir el entorno gráfico de Cypress (Test Runner)
npx cypress open

```

## 👨‍🏫 Docente

* **Docente:** Diego Wolf
* **Tutora:** Tatiana Tablada

## 👨‍💻 Autor

**Nicolás A. Pannunzio** – Full Stack Developer & QA Specialist
🔗 [Perfil de LinkedIn](https://www.linkedin.com/in/nicolas-a-pannunzio-/)