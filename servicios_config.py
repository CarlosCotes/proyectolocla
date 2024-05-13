from datos import *
RUTA_BASE_DE_DATOS = "servicios.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)

def registrar_servicios():
    while True:
        print("-------------------------------------------------")
        print("¿Que servicio desea agregar?")
        print("Servicios moviles")
        print("1. postpago")
        print("2. Larga Distancia Internaciona")
        print("3. roaming internacional")
        print("Servicios hogar")
        print("4. tripleplay")
        print("5. planes de internet")
        print("6. planes de television")
        print("0. volver al menu de servicios")
        print("-------------------------------------------------")
        
        esc = str(input("Ingrese la opcion que requiera: "))
        if esc == "1":
            registrar_postpago(datos)
        elif esc == "2":
            registrar_prepago(datos)
        elif esc == "3":
            registrar_roaming_internacional(datos)
        elif esc == "4":
            registrar_tripleplay(datos)
        elif esc == "5":
            registrar_planes_de_internet(datos)
        elif esc == "6":
            registrar_planes_de_television(datos)
        elif esc == "0":
            print("volviendo")
            break

        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)


def eliminar_servicios():
    while True:
        print("-------------------------------------------------")
        print("¿Que servicio desea agregar?")
        print("Servicios moviles")
        print("1. postpago")
        print("2. Larga Distancia Internaciona")
        print("3. roaming internacional")
        print("Servicios hogar")
        print("4. tripleplay")
        print("5. planes de internet")
        print("6. planes de television")
        print("0. volver al menu de servicios")
        print("-------------------------------------------------")
        
        esc = str(input("Ingrese la opcion que requiera: "))
        if esc == "1":
            eliminar_postpago(datos)
        elif esc == "2":
            eliminar_prepago(datos)
        elif esc == "3":
            eliminar_roaming_internacional(datos)
        elif esc == "4":
            eliminar_tripleplay(datos)
        elif esc == "5":
            eliminar_planes_de_internet(datos)
        elif esc == "6":
            eliminar_planes_de_television(datos)
        elif esc == "0":
            print("volviendo")
            break

def mostrar_serviciome():
    RUTA_BASE_DE_DATOS = "tienda.json"
    datos = cargar_datos(RUTA_BASE_DE_DATOS)
    #Ramificaciones menu servicio
    print("-------------------------------------------------")
    print("Bienvenido al menu de para ver los servicios")
    print("1. ver todos los servicios")
    print("2. ver un servicio en especifico")
    print("0. volver al menu servicios")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            datos = mostrar_servicios(datos)
        elif opc == "2":
            datos = mostrar_servicio(datos)
        elif opc == "0":
            
            print("volviendo")
            break
    guardar_datos(datos,RUTA_BASE_DE_DATOS)           
def mostrar_servicios(datos):
    RUTA_BASE_DE_DATOS = "tienda.json"
    datos = cargar_datos(RUTA_BASE_DE_DATOS)
    print("¿Que servicios desea ver? ")
    prd = str(input("ingrese nombre de la catergoria : "))
    datos = (datos)
    print (prd)
    print("servicios disponibles")
    for i in range(len(datos[prd])):
        print(datos[prd][i]["referencia"], " - ", datos[prd][i]["precio"])
     
    guardar_datos(datos,RUTA_BASE_DE_DATOS)
def mostrar_servicio(datos1):
        datos1 = dict(datos1)
        referencia =input("Ingrese el referencia del servicio: ")
        for i in range(len(datos1["servicio"])):
            if datos1["servicio"][i]["referencia"] == referencia:
                print(datos1["servicio"][i])


































#Funciones para registrar
def registrar_prepago(datos):
    prepago={}
    prepago["referencia"]=input("Ingrese el referencia: ")
    prepago["precio"]=input("Ingrese el precio: ")

    print(datos["prepago"])
    datos["prepago"].append(prepago)
    print("prepago registrado con éxito!")
    return datos

def registrar_postpago(datos):
    postpago={}
    postpago["referencia"]=input("Ingrese el referencia: ")
    postpago["precio"]=input("Ingrese el precio: ")
    print(datos["postpago"])
    datos["postpago"].append(postpago)
    print("postpago registrado con éxito!")
    return datos

def registrar_roaming_internacional(datos):
    roaming_internacional={}
    roaming_internacional["referencia"]=input("Ingrese el referencia: ")
    roaming_internacional["precio"]=input("Ingrese el precio: ")
    print(datos["roaming_internacional"])
    datos["roaming_internacional"].append(roaming_internacional)
    print("roaming_internacional registrado con éxito!")
    return datos

def registrar_tripleplay(datos):
    tripleplay={}
    tripleplay["referencia"]=input("Ingrese el referencia: ")
    tripleplay["precio"]=input("Ingrese el precio: ")
    print(datos["tripleplay"])
    datos["tripleplay"].append(tripleplay)
    print("tripleplay registrado con éxito!")
    return datos

def registrar_planes_de_internet(datos):
    planes_de_internet={}
    planes_de_internet["referencia"]=input("Ingrese el referencia: ")
    planes_de_internet["precio"]=input("Ingrese el precio: ")
    print(datos["planes_de_internet"])
    datos["planes_de_internet"].append(planes_de_internet)
    print("planes_de_internet registrado con éxito!")
    return datos

def registrar_planes_de_television(datos):
    planes_de_television={}
    planes_de_television["referencia"]=input("Ingrese el referencia: ")
    planes_de_television["precio"]=input("Ingrese el precio: ")
    print(datos["planes_de_television"])
    datos["planes_de_television"].append(planes_de_television)
    print("planes_de_television registrado con éxito!")
    return datos

#Funciones para eliminar
def eliminar_prepago(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del prepago: ")
    for i in range(len(datos["prepago"])):
        if datos["prepago"][i]["referencia"] == referencia:
                datos["prepago"].pop(i)
                print("servicio eliminado!")
                return datos

def eliminar_postpago(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del postpago: ")
    for i in range(len(datos["postpago"])):
        if datos["postpago"][i]["referencia"] == referencia:
                datos["postpago"].pop(i)
                print("servicio eliminado!")
                return datos
            
def eliminar_roaming_internacional(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del roaming internacional: ")
    for i in range(len(datos["roaming_internacional"])):
        if datos["roaming_internacional"][i]["referencia"] == referencia:
                datos["roaming_internacional"].pop(i)
                print("servicio eliminado!")
                return datos
            
def eliminar_tripleplay(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del plan tripleplay: ")
    for i in range(len(datos["tripleplay"])):
        if datos["tripleplay"][i]["referencia"] == referencia:
                datos["tripleplay"].pop(i)
                print("servicio eliminado!")
                return datos

def eliminar_planes_de_internet(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del plan de internet: ")
    for i in range(len(datos["planes_de_internet"])):
        if datos["planes_de_internet"][i]["referencia"] == referencia:
                datos["planes_de_internet"].pop(i)
                print("servicio eliminado!")
                return datos

def eliminar_planes_de_television(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del plan de television: ")
    for i in range(len(datos["planes_de_television"])):
        if datos["planes_de_television"][i]["referencia"] == referencia:
                datos["planes_de_television"].pop(i)
                print("servicio eliminado!")
                return datos


