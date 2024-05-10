#Importaciones
from datos import *
RUTA_BASE_DE_DATOS = "productos_tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Eliminar productos de la tienda
def eliminar_audifonos(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del audifonos: ")
    for i in range(len(datos["audifonos"])):
        if datos["audifonos"][i]["referencia"] == referencia:
                datos["audifonos"].pop(i)
                print("producto eliminado!")
                return datos
    
def eliminar_televisor(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del televisor: ")
    for i in range(len(datos["televisor"])):
        if datos["televisor"][i]["referencia"] == referencia:
                datos["televisor"].pop(i)
                print("producto eliminado!")
                return datos

def eliminar_computador(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del computador: ")
    for i in range(len(datos["computador"])):
        if datos["computador"][i]["referencia"] == referencia:
                datos["computador"].pop(i)
                print("producto eliminado!")
                return datos
                        
def eliminar_apple(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del apple: ")
    for i in range(len(datos["apple"])):
        if datos["apple"][i]["referencia"] == referencia:
                datos["apple"].pop(i)
                print("producto eliminado!")
                return datos
            
def eliminar_samsung(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del samsung: ")
    for i in range(len(datos["samsung"])):
        if datos["samsung"][i]["referencia"] == referencia:
                datos["samsung"].pop(i)
                print("producto eliminado!")
                return datos            

def eliminar_motorola(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del motorola: ")
    for i in range(len(datos["motorola"])):
        if datos["motorola"][i]["referencia"] == referencia:
                datos["motorola"].pop(i)
                print("producto eliminado!")
                return datos

def eliminar_xiaomi(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del xiaomi: ")
    for i in range(len(datos["xiaomi"])):
        if datos["xiaomi"][i]["referencia"] == referencia:
                datos["xiaomi"].pop(i)
                print("producto eliminado!")
                return datos

def eliminar_tecno(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del tecno: ")
    for i in range(len(datos["tecno"])):
        if datos["tecno"][i]["referencia"] == referencia:
                datos["tecno"].pop(i)
                print("producto eliminado!")
                return datos
                                 
#Menu para escoger que producto se va a eliminar
def eliminar_producto():
    print("¿Que producto desea eliminar?")
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
        eliminar_audifonos(datos)
    elif esc == 2:
        eliminar_televisor(datos)
    elif esc == 3:
        eliminar_computador(datos)
    elif esc == 4:
        eliminar_apple(datos)
    elif esc == 5:
        eliminar_samsung(datos)
    elif esc == 6:
        eliminar_motorola(datos)
    elif esc == 7:
        eliminar_xiaomi(datos)
    elif esc == 8:
        eliminar_tecno(datos)
        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)  