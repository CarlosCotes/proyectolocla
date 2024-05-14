from datos import *
from excepciones import *
RUTA_BASE_DE_DATOS = "usuario.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
def actualizar_usuario(datos):
    try:
        datos=dict(datos)
        documento =input("Ingrese el documento del usuario: ")
        for i in range(len(datos["usuario"])):
            if datos["usuario"][i]["documento"]== documento:


                while True:
                    print("¿infomacion que requiera modificar")
                    print("0. para salir ")
                    print("1. para modificar el nombre: ")
                    print("2. para modificar el documento: ")
                    print("3. para modificar la direccion: ")
                    print("4. para modificar el telefono: ")

                    opc=input("ingrese la opcion: ")

                    if opc=="1":
                        datos["usuario"][i]["nombre"]= input("ingrese el nuevo nombre: ")
                        print("se guardo con exito")
                        print("------------------------------------------------")


                    elif opc== "2":
                        datos["usuario"][i]["documento"]=input("ingrese el nuevo documento: ")
                        print("se guardo con exito")
                        print("------------------------------------------------")

                    elif opc=="3":
                        datos["usuario"][i]["direccion"]= input("ingrese la nueva direccion: ")
                        print("se guardo con exito")
                        print("------------------------------------------------")
                        
                    elif opc=="4":
                        datos["usuario"][i]["telefono"]= input("ingrese el nuevo telefono: ")
                        print("se guardo con exito")
                        print("------------------------------------------------")

                    elif opc=="0":
                        break
            return datos
    except Exception as e:
        log_error(e, "../Errores.txt")
def registrar_usuarioadm(datos:dict):
    try:
        usuario={}
        usuario["nombre"]=input("Ingrese el nombre: ")
        usuario["documento"]=input("Ingrese el documento: ")
        usuario["numero telefonico"]=input("Ingrese su numero telefono ")
        usuario["direccion"]=input("Ingrese su direccion ")
        usuario["tipo de usuario"]=input(("nuevo"))
        datos["usuario"].append(usuario)
        print("usuario registrado con éxito!")
        return datos
    except Exception as e:
        log_error(e, "../Errores.txt")
def eliminar_usuario(datos):
    try:
        datos = dict(datos)
        documento =input("Ingrese el documento del usuario: ")
        for i in range(len(datos["usuario"])):
            if datos["usuario"][i]["documento"] == documento:
                    datos["usuario"].pop(i)
                    print("usuario eliminado!")
                    return datos
    except Exception as e:
        log_error(e, "../Errores.txt")
def mostrar_usuariome():
    try:
        RUTA_BASE_DE_DATOS = "usuario.json"
        datos = cargar_datos(RUTA_BASE_DE_DATOS)
        #Ramificaciones menu usuario
        print("-------------------------------------------------")
        print("Bienvenido al menu de para ver los usuarios")
        print("1. ver todos los usuarios")
        print("2. ver un usuario en especifico")
        print("0. volver al menu usuario")
        print("-------------------------------------------------")
        while True:
            opc = str(input("Ingrese la opcion que requiera: "))
            if opc == "1":
                datos = mostrar_usuarios(datos)
            elif opc == "2":
                datos = mostrar_usuario(datos)
            elif opc == "0":
                
                print("volviendo")
                break
        guardar_datos(datos,RUTA_BASE_DE_DATOS)           
    except Exception as e:
        log_error(e)
def mostrar_usuarios(datos):
    try:
        datos = dict(datos)
        print("usuarios:")
        for i in range(len(datos["usuario"])):
            print(datos["usuario"][i]["nombre"], " - ", datos["usuario"][i]["documento"])
    except Exception as e:
        log_error(e, "../Errores.txt")
def mostrar_usuario(datos):
    try:
        datos = dict(datos)
        documento =input("Ingrese el documento del usuario: ")
        for i in range(len(datos["usuario"])):
            if datos["usuario"][i]["documento"] == documento:
                print(datos["usuario"][i])
    except Exception as e:
        log_error(e, "../Errores.txt")