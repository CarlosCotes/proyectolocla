from datos import *
from servicios_config import *
RUTA_BASE_DE_DATOS = "servicios.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def menu_servicios():
    #Ramificaciones menu servicios
    print("-------------------------------------------------")
    print("Bienvenido al menu de tienda que cambios requiere realizar")
    print("1. agregar productos a la tienda")
    print("2. eliminar productos de la tienda")
    print("3. actualiza productos de la tienda")
    print("4. mostrar productos de la tienda")
    print("0. volver al menu principal")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            print("volviendo")
            
            #datos = agregar_producto(datos)
        elif opc == "2":
            print("volviendo")
            
            #datos = eliminar_producto(datos)
        #elif opc == 3:
            #datos = actualizar_producto(datos)
        #elif opc == 4:
            
        elif opc == 0:
            
            print("volviendo")
            break
                
guardar_datos(datos,RUTA_BASE_DE_DATOS)