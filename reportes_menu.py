from datos import *
#constantes para cargar y guardar los datos en las carpetas
RUTA_BASE_DE_DATOS = "servicios.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)

while True:
    #Ramificaciones del menu administrativo
    print("-------------------------------------------------")
    print("Bienvenido al menu de reportes")
    print("opciones")
    print("1. gerenerar un reporte")
    print("2. eliminar un reporte")
    print("3. actualiza un reporte")
    print("4. mostrar menu para ver los reportes")
    print("0. volver menu administrador")
    print("-------------------------------------------------")
    opc = str(input("Ingrese la opcion que requiera: "))
    if opc == 1:
        print("1.")
    #elif opc == "4":
        
    elif opc == "0":
        print("volviendo")
        print("-------------------------------------------------")
        print("1. menu usuario")
        print("2. menu tienda")
        print("3. menu servicios")
        print("4. menu reportes")
        print("0. salir del menu")
        print("-------------------------------------------------")
            
        #break
guardar_datos(datos,RUTA_BASE_DE_DATOS)