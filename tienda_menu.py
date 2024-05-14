from datos import *
from tienda_config import *
RUTA_BASE_DE_DATOS = "tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def menu_tienda():
    #Ramificaciones menu tienda
    print("-------------------------------------------------")
    print("Bienvenido al menu de tienda que cambios requiere realizar")
    print("1. agregar productos a la tienda")
    print("2. eliminar productos de la tienda")
    print("3. actualiza productos de la tienda")
    print("4. mostrar menu para ver los productos")
    print("0. volver al menu principal")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            agregar_producto()
        elif opc == "2":
            eliminar_producto()
        elif opc == "3":
            actualizar_producto(datos)
        elif opc == "4":
            mostrar_productome()        
        elif opc == "0":
            print("volviendo")
            break
guardar_datos(datos,RUTA_BASE_DE_DATOS)
