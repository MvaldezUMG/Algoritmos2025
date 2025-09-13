"""
Crear un programa que dadas 4 notas de N cantidad de estudiantes
las cuales se ingresan separadas por comas, determine el promedio de cada estudiante.

Ejemplo:
Entrada          Salida
10,5,10,5         7.5
5,10,5,10         7.5
"""
promedios = []

while True:
    notas = input("Ingrese las notas separadas por coma \n")
    if notas == "salir":
        break
    notas_separadas = notas.split(",")
    if len(notas_separadas) != 4:
        print("Debe ingresar exactamente 4 notas")
        continue
    suma = 0
    for nota in notas_separadas:
        suma = suma + float(nota)
    promedio = suma / 4
    promedios.append(promedio)

print("Promedios")
print(promedios)