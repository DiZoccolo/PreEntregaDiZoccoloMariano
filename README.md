# _Tests automatizados sobre la pagina “https://www.saucedemo.com”_

## _Pre Requisitos_:

1. Pc.  
2. SO: WIN11.  
3. Conexion a internet.  
4. Navegador: Google Chrome.  
5. Interprete de python pre instalado (de no tenerlo descargar e instalar desde “https://www.python.org/downloads”).  
6. Visual Estudio Code (VSC). (de no tenerlo descargar e instalar desde “https://code.visualstudio.com”).  
7. Modulos de Pytest, Selenium, Webdriver y generador de reporte html pre instalados.  
(Para instalar correctamente las dependencias en VSC, debe escribir los siguientes comandos en la consola.  
Para instalar Pytest, escribir el siguiente comando “pip install pytest“.  
Para instalar Selenium, escribir el siguiente comando “pip install selenium”.  
Para instalar Webdriver, escribir el siguiente comando “pip install webdriver-manager”.  
Para instalar generador de reporte html, escribir el siguiente comando “pip install pytest-html”).  

## _Objetivo_: 
El objetivo de este proyecto es automatizar pruebas de:  

1. Login exitoso.
2. Comprobación de titulo de la pagina web.
3. Verificación de existencia de almenos un prodcuto en la pagina “https://www.saucedemo.com/inventory.html”.
4. Verificación de existencia y visibilidad de menu, filtro de búsqueda, footer.
5. Comprobación de actualización de carrito de compras al añadir un producto existente.

## _Ejecución de pruebas_:  
Para ejecutar las pruebas, dirigirse al archivo “runs_tests.py”, abrirlo en VSC, ejecutar dicho archivo. Este correrá las pruebas correspondientes y posteriormente generara un reporte, “report.html”
