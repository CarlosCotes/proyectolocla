def newusuario():
    print("*************************************************")
    print("Bienvenido al menu principal de claro ")
    print("")
    usu = int(input("Ingrese una opcion: "))
    if usu=="N":
        print("No")
    

    
    
    
def pedir_opcion():
    pr = 0
    try:
        pr = int(input("Ingrese su opción: "))
        print("***************************************")
        return pr
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1