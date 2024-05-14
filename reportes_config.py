
def generar_reportes(datos:dict):
    reporte={}
    reporte["numero_de_reportes"]=input("Ingrese el numero_de_reportes: ")
    reporte["Fecha"]=input("Ingrese la fecha: ")
    reporte["reporte"]=input("Desarrolle el reporte")
    datos["reporte"].append(reporte)
    print("reporte registrado con éxito!")
    return datos

def eliminar_reporte(datos):
    datos = dict(datos)
    Nreporte =input("Ingrese el #Reporte: ")
    for i in range(len(datos["reporte"])):
        if datos["reporte"][i]["#reporte"] == Nreporte:
                datos["reporte"].pop(i)
                print("reporte eliminado!")
                return datos
        

