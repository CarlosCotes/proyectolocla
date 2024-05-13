from datos import *
def actualizar_usuario(datos):
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
def registrar_usuarioadm(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["numero telefonico"]=input("Ingrese su numero telefono ")
    usuario["direccion"]=input("Ingrese su direccion ")
    usuario["tipo de usuario"]=input(("nuevo"))
    datos["usuario"].append(usuario)
    print("usuario registrado con éxito!")
    return datos

def eliminar_usuario(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del usuario: ")
    for i in range(len(datos["usuario"])):
        if datos["usuario"][i]["documento"] == documento:
                datos["usuario"].pop(i)
                print("Participante eliminado!")
                return datos

def mostrar_usuariome():
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
        opc = int(input("Ingrese la opcion que requiera: "))
        if opc == 1:
            datos = mostrar_usuarios(datos)
        elif opc == 2:
            datos = mostrar_usuario(datos)
        elif opc == 0:
            
            print("volviendo")
            break
    guardar_datos(datos,RUTA_BASE_DE_DATOS)           

def mostrar_usuarios(datos):
        datos = dict(datos)
        print("usuarios:")
        for i in range(len(datos["usuario"])):
            print(datos["usuario"][i]["nombre"], " - ", datos["usuario"][i]["documento"])

def mostrar_usuario(datos1):
        datos1 = dict(datos1)
        documento =input("Ingrese el documento del usuario: ")
        for i in range(len(datos1["usuario"])):
            if datos1["usuario"][i]["documento"] == documento:
                print(datos1["usuario"][i])
