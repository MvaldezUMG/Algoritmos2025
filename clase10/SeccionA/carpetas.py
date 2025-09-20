import os

def crear_carpeta(nombre):
    carpeta_existe = os.path.exists(nombre)

    if not carpeta_existe:
        os.makedirs(nombre)

def eliminar_carpeta(nombre):
    carpeta_existe = os.path.exists(nombre)
    
    if not carpeta_existe:
        print("La carpeta no existe")
        return
    
    os.removedirs(nombre)

def crear_carpeta_con_archivo(carpeta, nombre_archivo):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    ruta_completa = os.path.join(carpeta, nombre_archivo)
    archivo = open(ruta_completa, "w+")
    archivo.write("Hola desde mi programa")
    archivo.close()

def listar_carpetas(carpeta):
    lista = os.listdir(carpeta)
    carpetas = []
    for documento in lista:
        if os.path.isdir(documento):
            carpetas.append(documento) 
    print(carpetas)

crear_carpeta("PRUEBA")
eliminar_carpeta("PRUEBA")
eliminar_carpeta("PRUEBA2")
crear_carpeta_con_archivo("micarpeta", "archivo.txt")
listar_carpetas(None)