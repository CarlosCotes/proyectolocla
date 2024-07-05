# CLARO

### Descripcion
El repositorio cuenta con un software para una operadora

Este software contiene multiples funciones tanto para un usuarios como para un administrador.  
***
## Tabla de contenido
| Indice |  |
|--|--|
| 1 | [Descripcion](#Descripcion) |
| 2 | [Informacion general](#Informacion-general)|
| 3 | [Instalacion](#Instalacion) |
| 4 | [Tecnologias utilizadas](#Tecnologias-utilizadas) |
| 5 | [Hecho por](#Desarrollador)|
| 6 | [Mensaje del desarrollador](#Mensaje-del-desarrollador)|

***
> [!IMPORTANT]  
>
>### Informacion-general
> El desarrollo del software cuenta con dos modulos principales los cuales tienen funciones diferentes los cuales son modulo de usuario y modulo de administrador. el modulo de usuario cuenta con requerimientos basico como
>
>* Creacion de perfil
>* eliminacion del perfil
>* Actualizacion del perfil
>* visualizacion del perfil
>
> **El menu de usuario le permite realizar las siguentes funciones**
>
>* Adquirir un servicio
>* Visualizar los servicio
>* Comprar un producto
>* Visualizar los productos
>
> **En cuanto al modulo del administrador permite**
>* Creacion de un perfiles
>* eliminacion de perfiles
>* actualizar informacion de perfiles
>* visualizar los perfiles
>
>  **El menu de administrador le permite realizar las siguentes funciones**
>
>* Creacion de servicios
>* Eliminar servicios
>* Actualizar la informacion de los servicios
>* Visualizar los servicios
>
>* Creacion de productos
>* Eliminar productos
>* Actualizar la informacion de los productos
>* Visualizar los productos
>
>* Creacion de reportes de ventas
>* Eliminar reportes de venta
>* Actualizar la informacion de los reportes de ventas
>* Visualizar los reportes
>
> para cargar los datos y guardar se uso la siguentes funciones
> 
```bash
>import json
>
>def cargar_datos(archivo):
>    datos = {}
>    with open(archivo,"r") as file:
>        datos=json.load(file)
>    return datos
>        
>        
>
>def guardar_datos(datos, archivo):
>    datos = dict(datos)
>    
>    diccionario=json.dumps(datos, indent=4)
>    file=open(archivo,"w")
>    file.write(diccionario)
>    file.close()
```
> [!IMPORTANT]
> La cual se encarga de utilizar archivos json para guardar diccionarios con informacion esta funcion se utiliza en fuciones como
>   
```bash
>from datos import *
>
>RUTA_BASE_DE_DATOS = "tienda.json"
>datos = cargar_datos(RUTA_BASE_DE_DATOS)
>#Menu para escoger que producto se va a añadir
>def agregar_producto():
>        print("-------------------------------------------------")
>        print("¿Que producto desea agregar?")
>        print("Tecnologia")
>        print("1. audifonos")
>        print("2. Televisores")
>        print("3. computadores")
>        print("Celulares")
>        print("4. apple")
>        print("5. Samsumg")
>        print("6. Motorola")
>        print("7. Xiaomi")
>        print("8. Tecno")
>        print("-------------------------------------------------")
>        esc = int(input("Ingrese la opcion que requiera: "))
>        if esc == 1:
>            registrar_audifonos(datos)
>        elif esc == 2:
>            registrar_televisor(datos)
>        elif esc == 3:
>            registrar_computador(datos)
>        elif esc == 4:
>            registrar_apple(datos)
>        elif esc == 5:
>            registrar_samsung(datos)
>        elif esc == 6:
>            registrar_motorola(datos)
>        elif esc == 7:
>            registrar_xiaomi(datos)
>        elif esc == 8:
>            registrar_tecno(datos)
>            
>        guardar_datos(datos,RUTA_BASE_DE_DATOS)
```
> [!IMPORTANT]
> no se busca continuar con el proyecto o solucionar problemas que presenta actualmente en base a esta informacion no recibira actualizaciones el repositorio
>
>### Instalacion
>
>1. Descargar el archivo zip desde el repositorio
>2. Descomprimir el archivo zip
>3. Abrir la carpeta desde visual estudio code
>4. Iniciar el terminal desde el archivo menu_adm.py o menu_usuario.py
>  
>### Tecnologias-utilizadas
>Lista de lenguajes en los cuales se desarrollo
>* [Python](Python): Version: 3.12.2 
>

***
> [!WARNING]  
> 
>### Desarrollador
>* [Carlos Cotes](https://gist.github.com/CarlosCotes)
>
***
> [!NOTE]
>### Mensaje-del-desarrollador
>Gracias por ver este repositorio

