#Importaciones
from datos import *
RUTA_BASE_DE_DATOS = "productos_tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Añadir productos a la tienda
def registrar_audifonos(datos):
    audifonos={}
    audifonos["referencia"]=input("Ingrese el referencia: ")
    audifonos["precio"]=input("Ingrese el precio: ")
    audifonos["fabricante"]=input("Ingrese el fabricane ")
    audifonos["direccion"]=input("Ingrese la garantia ")
    print(datos["audifonos"])
    datos["audifonos"].append(audifonos)
    print("audifonos registrado con éxito!")
    return datos

def registrar_televisor(datos):
    televisor={}
    televisor["referencia"]=input("Ingrese el referencia: ")
    televisor["precio"]=input("Ingrese el precio: ")
    televisor["fabricante"]=input("Ingrese el fabricane ")
    televisor["direccion"]=input("Ingrese la garantia ")
    print(datos["televisor"])
    datos["televisor"].append(televisor)
    print("televisor registrado con éxito!")
    return datos
def registrar_computador(datos):
    computador={}
    computador["referencia"]=input("Ingrese el referencia: ")
    computador["precio"]=input("Ingrese el precio: ")
    computador["fabricante"]=input("Ingrese el fabricane ")
    computador["direccion"]=input("Ingrese la garantia ")
    print(datos["computador"])
    datos["computador"].append(computador)
    print("computador registrado con éxito!")
    return datos

def registrar_apple(datos):
    apple={}
    apple["referencia"]=input("Ingrese el referencia: ")
    apple["precio"]=input("Ingrese el precio: ")
    apple["fabricante"]=input("Ingrese el fabricane ")
    apple["direccion"]=input("Ingrese la garantia ")
    print(datos["apple"])
    datos["apple"].append(apple)
    print("apple registrado con éxito!")
    return datos

def registrar_samsung(datos):
    samsung={}
    samsung["referencia"]=input("Ingrese el referencia: ")
    samsung["precio"]=input("Ingrese el precio: ")
    samsung["fabricante"]=input("Ingrese el fabricane ")
    samsung["direccion"]=input("Ingrese la garantia ")
    print(datos["samsung"])
    datos["samsung"].append(samsung)
    print("samsung registrado con éxito!")
    return datos

def registrar_motorola(datos):
    motorola={}
    motorola["referencia"]=input("Ingrese el referencia: ")
    motorola["precio"]=input("Ingrese el precio: ")
    motorola["fabricante"]=input("Ingrese el fabricane ")
    motorola["direccion"]=input("Ingrese la garantia ")
    print(datos["motorola"])
    datos["motorola"].append(motorola)
    print("motorola registrado con éxito!")
    return datos

def registrar_xiaomi(datos):
    xiaomi={}
    xiaomi["referencia"]=input("Ingrese el referencia: ")
    xiaomi["precio"]=input("Ingrese el precio: ")
    xiaomi["fabricante"]=input("Ingrese el fabricane ")
    xiaomi["direccion"]=input("Ingrese la garantia ")
    print(datos["xiaomi"])
    datos["xiaomi"].append(xiaomi)
    print("xiaomi registrado con éxito!")
    return datos

def registrar_tecno(datos):
    tecno={}
    tecno["referencia"]=input("Ingrese el referencia: ")
    tecno["precio"]=input("Ingrese el precio: ")
    tecno["fabricante"]=input("Ingrese el fabricane ")
    tecno["direccion"]=input("Ingrese la garantia ")
    print(datos["tecno"])
    datos["tecno"].append(tecno)
    print("tecno registrado con éxito!")
    return datos
#Menu para escoger que producto se va a añadir
def añadir_producto():
    print("¿Que producto desea agregar?")
    print("Tecnologia")
    print("1.audifonos")
    print("2.Televisores")
    print("3.computadores")
    print("Celulares")
    print("4.apple")
    print("5.Samsumg")
    print("6.Motorola")
    print("7.Xiaomi")
    print("8.Tecno")
    esc = int(input("Ingrese la opcion que requiera: "))
    if esc == 1:
        registrar_audifonos(datos)
    elif esc == 2:
        registrar_televisor(datos)
    elif esc == 3:
        registrar_computador(datos)
    elif esc == 4:
        registrar_apple(datos)
    elif esc == 5:
        registrar_samsung(datos)
    elif esc == 6:
        registrar_motorola(datos)
    elif esc == 7:
        registrar_xiaomi(datos)
    elif esc == 8:
        registrar_tecno(datos)
        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)   