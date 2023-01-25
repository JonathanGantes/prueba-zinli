# prueba-zinli

Paso 1: Dependencias
Instalar Python 3
Ejecutar en cmd desde el repositorio para instalar dependencias: pip install -r requeriments.txt

Paso 2: Configurar Pytest.ini

Con BrowserStack:
Abrir el Pyest.ini y colocar las credenciales de BSTACK y el app id (debe subir el app a su browserstack)

Con Emulador Local:
Colocar el Nombre de su dispositivo emulado y recodar tener appium server corriendo, (se probo con un pixel 6 api 30)

Paso 4: Ejecutar las pruebas
Comando: pytest -m "test" .\pytest.dev.ini --gherkin-terminal-reporter -vv -s