#Importaciones de otros archivos para usarlos en este y unirlos
from datos import *
from usuario_menu import *
from usuario_config import *
from tienda_menu import *
from tienda_config import *
from servicios_menu import *

#constantes para cargar y guardar los datos en las carpetas
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
try:
    while True:
        #Ramificaciones del menu administrativo
        print("-------------------------------------------------")
        print("Bienvenido al menu administrador")
        print("1. menu usuario")
        print("2. menu tienda")
        print("3. menu servicios")
        print("4. menu reportes")
        print("0. salir del menu")
        print("-------------------------------------------------")
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            menu_usuario()
        elif opc == "2":
            menu_tienda()
        elif opc == "3":
            datos = eliminar_usuario(datos)

        elif opc == "0":
            
            print("¡Buen trabajo!")
            break
except Exception:
            print("Valor inválido")
            print("-------------------------------------------------")
guardar_datos(datos,RUTA_BASE_DE_DATOS)

    
    
    
    