def registrar_apple(datos:dict):
    apple={}
    apple["nombre"]=input("Ingrese el nombre: ")
    apple["precio"]=input("Ingrese el precio: ")
    apple["fabricante"]=input("Ingrese el fabricane ")
    apple["direccion"]=input("Ingrese la garantia ")
    print(datos["apple"])
    datos["apple"].append(apple)
    print("apple registrado con éxito!")
    return datos

def registrar_samsung(datos:dict):
    samsung={}
    samsung["nombre"]=input("Ingrese el nombre: ")
    samsung["precio"]=input("Ingrese el precio: ")
    samsung["fabricante"]=input("Ingrese el fabricane ")
    samsung["direccion"]=input("Ingrese la garantia ")
    print(datos["samsung"])
    datos["samsung"].append(samsung)
    print("samsung registrado con éxito!")
    return datos