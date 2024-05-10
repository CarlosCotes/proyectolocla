def registrar_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["numero telefonico"]=input("Ingrese su numero telefono ")
    usuario["direccion"]=input("Ingrese su direccion ")
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
            
def registrar_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["numero telefonico"]=input("Ingrese su numero telefono ")
    usuario["direccion"]=input("Ingrese su direccion ")
    datos["usuario"].append(usuario)
    print("usuario registrado con éxito!")
    return datos