from datos import *
from servicios_config import *
RUTA_BASE_DE_DATOS = "servicios.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def menu_servicios():
    #Ramificaciones menu servicios
    print("-------------------------------------------------")
    print("Bienvenido al menu de servicios que cambios requiere realizar")
    print("1. agregar servicios")
    print("2. eliminar servicios")
    print("3. actualiza servicios")
    print("4. mostrar servicios")
    print("0. volver al menu principal")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            registrar_servicios()
        elif opc == "2":
            eliminar_servicios()
        elif opc == 3:
            datos = actualizar_servicios(datos)
        elif opc == "4":
            mostrar_serviciome()
        elif opc == "0":
            
            print("volviendo")
            print("opciones")
            print("-------------------------------------------------")
            print("1. menu usuario")
            print("2. menu tienda")
            print("3. menu servicios")
            print("4. menu reportes")
            print("0. salir del menu")
            print("-------------------------------------------------")
            
            break
                
guardar_datos(datos,RUTA_BASE_DE_DATOS)