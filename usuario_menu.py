from datos import *
from usuario_config import *
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def menu_usuario():
    #Ramificaciones menu usuario
    print("-------------------------------------------------")
    print("Bienvenido al menu de usuario que cambios requiere realizar")
    print("1. agregar usuario")
    print("2. eliminar usuario")
    print("3. actualiza informacion de un usuario")
    print("4. mostrar menu para ver los usuarios")
    print("0. volver al menu principal")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            registrar_usuarioadm(datos)
        elif opc == "2":
            eliminar_usuario(datos)
        elif opc == "3":
            actualizar_usuario(datos)
        elif opc == "4":
            mostrar_usuariome()
        elif opc == "0":
            
            print("volviendo")
            break
               
