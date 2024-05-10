def newusuario():
    print("menu al cual desea ser trasladado")
    print("1. Tienda")
    print("2. Servicios claro")  
    print("3. manejo de tu cuenta claro")


def pedir_opcion():
    pr = 0
    try:
        pr = float(input("Ingrese su opción: "))
        print("-------------------------------------------------")
        return pr
    except Exception:
        print("Valor inválido")
        print("-------------------------------------------------")
        return -1
    #    usu = float(input("Ingrese una opcion: "))
    #if usu=="N":
        #print("No")