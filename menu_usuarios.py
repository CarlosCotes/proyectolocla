from datos import *
from usuario_config import *
from tienda_config import*
from servicios_config import *
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
print("-------------------------------------------------")
print("Bienvenido a claro")
print("¿es usuario claro?")


while True:
    usu = str(input("S/SI-N/NO: "))
    print("-------------------------------------------------")
    if usu == "N":
        registrar_usuario(datos)
    elif usu == "S":
        break
    else:
        print("Ingrese una opcion valida para continuar")
while True:
    try:
        print("-------------------------------------------------")
        print("Bienvenido usuario claro")
        print("1. actualizar datos en cuenta claro")
        print("2 elimininar cuenta claro")
        print("3. comprar en la tienda")
        print("4. comprar un servicio")
        print("0. salir")
        print("-------------------------------------------------")
        opc= str(input("Ingrese una opcion: "))
        if opc == "1":
           actualizar_usuario()
        elif opc == "2":
            eliminar_usuario() 
        elif opc == "3":
            comprar_producto()
        elif opc == "4":
            comprar_serviciosas()
        elif opc == "0":
            print("Gracias por preferirnos")
            break
        guardar_datos(datos,RUTA_BASE_DE_DATOS)
    except Exception as e:
        log_error(e)