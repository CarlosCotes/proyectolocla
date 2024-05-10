from datos import *
from menu import *
from usuario import *
from aggprd import *

#Constants


RUTA_BASE_DE_DATO = "productos_ventas.json"
datos1 = cargar_datos(RUTA_BASE_DE_DATO)
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)

newusuario()

while True:
    pr = pedir_opcion()
    if pr == 1:
        datos = registrar_usuario(datos)
    elif pr ==2:
        print("2")
    elif pr == 11:
        print("gracias por preferirnos")
        break
guardar_datos(datos, RUTA_BASE_DE_DATOS)
guardar_datos(datos1, RUTA_BASE_DE_DATO)