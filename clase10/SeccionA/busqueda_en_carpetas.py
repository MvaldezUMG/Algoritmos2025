"""
Crear un programa en Python, que dado una ruta de carpeta
y un texto, busque en todos los archivos .txt dentro de la ruta
e indique en cual archivo encontro lo que buscaba.
"""
import os
import sys
import shutil

def listar_carpetas(carpeta_principal):
    #Devuelve todo tanto archivos como carpetas.
    archivos = os.listdir(carpeta_principal)
    print(archivos)
    carpetas = []
    for archivo in archivos:
        if os.path.isdir(os.path.join(carpeta_principal, archivo)):
            carpetas.append(archivo)

    return carpetas

def listar_archivos(ruta, extension):
    archivos = os.listdir(ruta)
    filtrados = []
    for archivo in archivos:
        if extension in archivo:
            filtrados.append(archivo)
    return filtrados

def buscar_en_archivos(ruta_principal, texto_a_buscar):
    carpetas = listar_carpetas(ruta_principal)
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta_principal, carpeta)
        archivos = listar_archivos(ruta_carpeta, ".txt")
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            datos_archivo = open(ruta_archivo, "r")
            texto_archivo = datos_archivo.read()
            if texto_a_buscar in texto_archivo:
                print("Datos encontrados en archivo " + ruta_archivo)

def mover_archivo(origen, destino):
    shutil.move(origen, destino)

if len(sys.argv) > 2:
    carpeta = sys.argv[1]
    valor_a_buscar = sys.argv[2]
    buscar_en_archivos(carpeta, valor_a_buscar)

#mover_archivo("ejemplo/1", "micarpeta")
mover_archivo("micarpeta/1", "ejemplo")