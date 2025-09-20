import os

def carpetas(nombre, archivo):
    #Verificar si la carpeta existe
    if not os.path.exists(nombre):
        #Creamos la carpeta
        os.makedirs(nombre)
    
    nombre_completo = os.path.join(nombre, archivo)
    archivo = open(nombre_completo, "w+")
    archivo.write("Hola desde mi programa")
    archivo.close()

carpetas("prueba", "prueba.txt")