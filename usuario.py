def actualizar_usuario(datos):
    datos=dict(datos)
    documento =input("Ingrese el documento del cliente a remplazar: ")
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
    usuario["tipo de usuario"]=input("ingrese si el usuario es nuevo , leal o regular  ")
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
#def manejo_de_cuenta():
    