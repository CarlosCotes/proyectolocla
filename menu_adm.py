#Importaciones de otros archivos para usarlos en este y unirlos
from datos import *
from excepciones import *
from usuario_config import *
from tienda_config import *
from servicios_config import *
from reportes_config import *

#constantes para cargar y guardar los datos en las carpetas
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
try:
    while True:
        #Ramificaciones del menu administrativo
        print("-------------------------------------------------")
        print("Bienvenido al menu administrador")
        print("usuarios")
        print("1. agregar usuario")
        print("2. eliminar usuario")
        print("3. actualiza informacion de un usuario")
        print("4. mostrar menu para ver los usuarios")
        print("Tienda")
        print("5. agregar productos a la tienda")
        print("6. eliminar productos de la tienda")
        print("7. actualiza productos de la tienda")
        print("8. mostrar menu para ver los productos")
        print("Servicios")
        print("9. agregar servicios")
        print("10. eliminar servicios")
        print("11. actualiza servicios")
        print("12. mostrar servicios")
        print("Reportes")
        print("13. gerenerar un reporte")
        print("14. eliminar un reporte")
        print("15. actualiza un reporte")
        print("16. mostrar menu para ver los reportes")
        print("0. salir del menu")
        print("-------------------------------------------------")
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            registrar_usuarioadm(datos)
        elif opc == "2":
            eliminar_usuario(datos)
        elif opc == "3":
            actualizar_usuario(datos)
        elif opc == "4":
            mostrar_usuariome()
        elif opc == "5":
            agregar_producto()
        elif opc == "6":
            eliminar_producto()
        elif opc == "7":
            actualizar_producto()
        elif opc == "8":
            mostrar_productome()    
        elif opc == "9":
            registrar_servicios()
        elif opc == "10":
            eliminar_servicios()
        elif opc == "11":
            actualizar_servicios()
        elif opc == "12":
            mostrar_serviciome()
        elif opc == "13":
            generar_reportes()
        elif opc == "14":
            eliminar_reporte()
        elif opc == "15":
            actualizar_servicios()
        elif opc == "16":
            mostrar_serviciome()    
                
        elif opc == "0":
            print("¡Buen trabajo!")
            break
        guardar_datos(datos,RUTA_BASE_DE_DATOS)
except Exception as e:
    log_error(e)
    
    
      
    