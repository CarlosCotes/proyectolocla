#Importaciones
from datos import *
RUTA_BASE_DE_DATOS = "tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Añadir productos a la tienda
def registrar_audifonos(datos):
    audifonos={}
    audifonos["referencia"]=input("Ingrese el referencia: ")
    audifonos["precio"]=input("Ingrese el precio: ")
    audifonos["fabricante"]=input("Ingrese el fabricane ")
    audifonos["direccion"]=input("Ingrese la garantia ")
    audifonos["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles ")
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
    televisor["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles ")
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
    computador["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles ")
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
    apple["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles: ")
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
    samsung["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles: ")
    
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
    motorola["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles: ") 
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
    xiaomi["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles: ")
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
    tecno["articulos disponibles"]=input("Ingrese la cantinda de articulos disponibles: ")
    print(datos["tecno"])
    datos["tecno"].append(tecno)
    print("tecno registrado con éxito!")
    return datos
#Menu para escoger que producto se va a añadir
def agregar_producto():
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
    

    
    
def mostrar_productos():
    print("¿Que productos desea ver? ")
    prd = str(input("ingrese nombre de la catergoria : "))
    datos = (datos)
    print (prd)
    print("Productos disponibles")
    for i in range(len(datos[prd])):
        print(datos[prd][i]["referencia"], " - ", datos[prd][i]["cantidad disponible"])
     
    guardar_datos(datos,RUTA_BASE_DE_DATOS)

#actualizar           



#eliminar
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