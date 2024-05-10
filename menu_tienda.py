from datos import *

RUTA_BASE_DE_DATOS = "productos_tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def menu_tienda():
    print("-------------------------------------------------")
        
    print("Bienvenido a la tienda claro ")
    print("Tecnologia")
    print("1.audifonos")
    print("2.Televisores")
    print("3.computadores")
    print("-------------------------------------------------")
        
    print("Celulares")
    print("4.apple")
    print("5.Samsumg")
    print("6.Motorola") 
    print("7.Xiaomi")
    print("8.Tecno")
        
    print("-------------------------------------------------")
    opc = str(input("que articulos desea ver: "))
    if opc == "audifonos":
         print("mostrar_productos")

