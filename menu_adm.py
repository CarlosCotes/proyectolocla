from datos import *
from menu import *
from usuario import *
from aggprd import *
from menu_adm import *
from menu_tienda import *
from menu_servicios import *

def men_adm():
    print("-------------------------------------------------")
    print("Bienvenido al modo administrador")
    print("ingrese la opcion que requiera")
    print("1. registrar usuario")
    print("2. actualizar usuario")
    print("3. eliminar usuario")
    print("4. mostrar usuarios de claro")
    print("5. ver historial de compras de usuario")
    print("6. ver reportes")
    print("7. agregar productos a la tienda")
    print("8. eliminar productos de la tienda")
    print("-------------------------------------------------")
while True:
    opc = int(input("Ingrese la opcion que requiera: "))
    if opc == 1:
        registrar_usuario(datos)
    elif opc == 3:
        eliminar_usuario(datos)
    elif opc == 0:
            print("gracias por preferirnos")
            break


    
    
    
    