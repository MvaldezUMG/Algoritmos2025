"""
Escriba un programa que pida notas y
genere un promedio de todas las notas ingresadas.

Entradas                     Salidas
Numero ... N veces Real     Promedio como Real

Tabla de verificacion:
Entrada                 Salida
5,5,5,5,5,5,5,5,5,5,-1    5
"""
print("Ingrese una nota")
nota = float(input())
acumulado = nota
contador_de_notas = 1
while nota != -1:
    print("Ingrese una nota")
    nota = float(input())
    acumulado = acumulado + nota
    contador_de_notas = contador_de_notas + 1
print(f"El promedio es {acumulado /contador_de_notas}")