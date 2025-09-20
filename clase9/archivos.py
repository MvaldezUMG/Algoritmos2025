
def crear_archivo(nombre):
    archivo = open(nombre, "w")
    archivo.write("Hola")

    #Cerrar archivos
    archivo.close()

    #Abre el archivo y lo cierra de forma automatica
    with open(nombre, "w") as archivo:
        archivo.write("Hola otra vez")
    #El archivo queda cerrado

def agregar_al_archivo(nombre):
    #Modo "append" que significa añadir al final
    archivo = open(nombre, "a")
    archivo.write("\nEsta es una linea extra")
    archivo.close()

crear_archivo("hola.txt")
agregar_al_archivo("hola.txt")