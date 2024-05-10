#Importaciones
from datos import *
RUTA_BASE_DE_DATOS = "productos_tienda.json"
datos = cargar_datos(RUTA_BASE_DE_DATOS)
#Añadir productos a la tienda

def eliminar_apple(datos):
    datos = dict(datos)
    referencia =input("Ingrese la referencia del apple: ")
    for i in range(len(datos["apple"])):
        if datos["apple"][i]["referencia"] == referencia:
                datos["apple"].pop(i)
                print("apple eliminado!")
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
    #if esc == 1:
        #eliminar_audifonos(datos)
    #elif esc == 2:
        #eliminar_televisor(datos)
    #elif esc == 3:
        #eliminar_computador(datos)
    if esc == 4:
        eliminar_apple(datos)
    #elif esc == 5:
        #eliminar_samsung(datos)
    #elif esc == 6:
        #eliminar_motorola(datos)
    #elif esc == 7:
        #eliminar_xiaomi(datos)
    #elif esc == 8:
        #eliminar_tecno(datos)
        
    guardar_datos(datos,RUTA_BASE_DE_DATOS)  