"""
Crear un programa que incluyendo un argumento en la linea de comandos
que incluya las notas de N cantidad de estudiantes separadas por coma y a la vez
cada bloque de notas separados por @, genere una lista con el promedio de cada bloque,
ejemplo:
python promedios_linea_de_comando.py 3,5,6,7@4,7,9,3@5,3,2,3 
Resultado:
lista = [p1,p2,p3,etc]
"""
import sys

lista_promedios = []
datos = sys.argv[1]
bloques_de_notas = datos.split("@")
#print(bloques_de_notas)
for bloque in bloques_de_notas:
    notas_separadas = bloque.split(",")
    #print(notas_separadas)
    suma_de_bloque = 0
    for nota in notas_separadas:
        suma_de_bloque += float(nota)
    lista_promedios.append(suma_de_bloque / len(notas_separadas))

print(lista_promedios)