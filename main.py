#Imports
from datos import *
from menu import *
from usuario import *
from aggprd import *
from menu_tienda import *
from menu_servicios import *
from menu_adm import *

#Constants
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)

print("-------------------------------------------------")
print("Bienvenido al menu principal de claro ")
print("¿es usuario claro? S/SI.N/NO")
usu =str(input())
if usu == "N":
    registrar_usuario(datos)
elif usu == "3.1416":
    datos = men_adm()
else:
    newusuario()
while True:
    pr = pedir_opcion()
    if pr == 1:
       menu_tienda()
    elif pr == 2:
        menu_servicios()
    elif pr == 11:
        print("gracias por preferirnos")
        break
guardar_datos(datos,RUTA_BASE_DE_DATOS)