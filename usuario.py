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
    documento =input("Ingrese el documento del participante: ")
    for i in range(len(datos["participantes"])):
        if datos["participantes"][i]["documento"] == documento:
            if datos["participantes"][i]["pago"] == False:
                datos["participantes"].pop(i)
                print("Participante eliminado!")
                return datos