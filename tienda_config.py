#Importaciones
from datos import *
RUTA_BASE_DE_DATOS = "tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Menu para escoger que producto se va a añadir
def agregar_producto():
    print("-------------------------------------------------")
    print("¿Que producto desea agregar?")
    print("Tecnologia")
    print("1. audifonos")
    print("2. Televisores")
    print("3. computadores")
    print("Celulares")
    print("4. apple")
    print("5. Samsumg")
    print("6. Motorola")
    print("7. Xiaomi")
    print("8. Tecno")
    print("-------------------------------------------------")
    esc = str(input("Ingrese la opcion que requiera: "))
    if esc == "1":
        registrar_audifonos(datos)
    elif esc == "2":
        registrar_televisor(datos)
    elif esc == "3":
        registrar_computador(datos)
    elif esc == "4":
        registrar_apple(datos)
    elif esc == "5":
        registrar_samsung(datos)
    elif esc == "6":
        registrar_motorola(datos)
    elif esc == "7":
        registrar_xiaomi(datos)
    elif esc == "8":
        registrar_tecno(datos)
        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)
    

    
def mostrar_productome():
    RUTA_BASE_DE_DATOS = "tienda.json"
    datos = cargar_datos(RUTA_BASE_DE_DATOS)
    #Ramificaciones menu producto
    print("-------------------------------------------------")
    print("Bienvenido al menu de para ver los productos")
    print("1. ver todos los productos")
    print("2. ver un producto en especifico")
    print("0. volver al menu producto")
    print("-------------------------------------------------")
    while True:
        opc = str(input("Ingrese la opcion que requiera: "))
        if opc == "1":
            datos = mostrar_productos(datos)
        elif opc == "2":
            datos = mostrar_producto(datos)
        elif opc == "0":
            
            print("volviendo")
            break
    guardar_datos(datos,RUTA_BASE_DE_DATOS)           
def mostrar_productos(datos):
    RUTA_BASE_DE_DATOS = "tienda.json"
    datos2 = cargar_datos(RUTA_BASE_DE_DATOS)
    print("¿Que productos desea ver? ")
    prd = str(input("ingrese nombre de la catergoria : "))
    datos2 = (datos2)
    print (prd)
    print("Productos disponibles")
    for i in range(len(datos2[prd])):
        print(datos2[prd][i]["referencia"], " - ", datos2[prd][i]["cantidad disponible"])
     
    guardar_datos(datos,RUTA_BASE_DE_DATOS)
def mostrar_producto(datos1):
        datos1 = dict(datos1)
        referencia =input("Ingrese el referencia del producto: ")
        for i in range(len(datos1["producto"])):
            if datos1["producto"][i]["referencia"] == referencia:
                print(datos1["producto"][i])
#actualizar           
def actualizar_producto(datos):
    datos=dict(datos)    
    print("------------------------------------------------")
    prd = str(input("que tipo de producto va a cambiar: "))
    referencia =input("Ingrese el referencia del producto: ")
    for i in range(len(datos[prd])):
        if datos[prd][i]["referencia"]== referencia:


            while True:
                print("¿infomacion que requiera modificar")
                print("1. para modificar el referencia: ")
                print("2. para modificar el precio: ")
                print("3. para modificar la fabricante: ")
                print("4. para modificar el Garantia: ")
                print("5. para modificar la cantidad disponible")
                print("0. para salir ")
                opc=input("ingrese la opcion: ")

                if opc=="1":
                    datos[prd][i]["referencia"]=input("ingrese la nuevo referencia: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")


                elif opc== "2":
                    datos[prd][i]["precio"]=input("ingrese el nuevo precio: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="3":
                    datos[prd][i]["fabricante"]= input("ingrese el nuevo fabricante: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")
                    
                elif opc=="4":
                    datos[prd][i]["garantia"]= input("ingrese la nueva garantia: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")
                
                elif opc=="5":
                    datos[prd][i]["cantidad_disponible"]= input("ingrese la nueva cantidad disponible: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="0":
                    print("volviendo")
                    break
                


#eliminar
def eliminar_producto():
    print("-------------------------------------------------")
    print("¿Que producto desea eliminar?")
    print("Tecnologia")
    print("1. audifonos")
    print("2. Televisores")
    print("3. computadores")
    print("Celulares")
    print("4. apple")
    print("5. Samsumg")
    print("6. Motorola")
    print("7. Xiaomi")
    print("8. Tecno")
    print("-------------------------------------------------")
    esc = str(input("Ingrese la opcion que requiera: "))
    if esc == "1":
        eliminar_audifonos(datos)
    elif esc == "2":
        eliminar_televisor(datos)
    elif esc == "3":
        eliminar_computador(datos)
    elif esc == "4":
        eliminar_apple(datos)
    elif esc == "5":
        eliminar_samsung(datos)
    elif esc == "6":
        eliminar_motorola(datos)
    elif esc == "7":
        eliminar_xiaomi(datos)
    elif esc == "8":
        eliminar_tecno(datos)
        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)

#Funciones para agregar productos
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
#Funciones para eliminar productos
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
        eliminar_tecno(datos)
