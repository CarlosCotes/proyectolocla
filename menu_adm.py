#Importaciones de otros archivos para usarlos en este y unirlos
from datos import *
from menu import *
from usuario import *
from aggprd import *
from menu_adm import *
from menu_tienda import *
from menu_servicios import *
from eliprd import *
#constantes para cargar y guardar los datos en las carpetas
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Ramificaciones del menu administrativo


print("-------------------------------------------------")
print("Bienvenido al menu administrador")
print("ingrese la opcion que requiera")
print("1. registrar usuario")
print("2. actualizar usuario")
print("3. eliminar usuario")
print("4. mostrar usuarios de claro")
print("5. ver historial de compras de usuario")
print("6. ver reportes")
print("7. agregar productos a la tienda")
print("8. eliminar productos de la tienda")
print("9. agregar servicios")
print("10. eliminar servicios")
print("-------------------------------------------------")
while True:
    opc = int(input("Ingrese la opcion que requiera: "))
    if opc == 1:
        registrar_usuarioadm(datos)
    elif opc == 2:
        print("2")
    elif opc == 3:
        eliminar_usuario(datos)
    elif opc == 4:
        print("4")
    elif opc == 5:
        print("5")
    elif opc == 7:
        añadir_producto()
    elif opc ==8:
        eliminar_producto()
    elif opc == 0:
        
        print("¡Buen trabajo!")
        break
            
guardar_datos(datos,RUTA_BASE_DE_DATOS)

    
    
    
    