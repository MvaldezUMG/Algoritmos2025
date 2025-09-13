"""
Escriba un programa que pida los valores de 10 notas 
de estudiantes y calcule el promedio.

Entradas                     Salidas
Numero ... 10 veces Real     Promedio como Real

Tabla de verificacion:
Entrada                 Salida
5,5,5,5,5,5,5,5,5,5       5
"""

acumulado = 0
for actual in range(0, 10):
    print(f"Ingrese la nota {actual + 1}")
    nota_actual = float(input()) #Lo convertimos a un numero real
    acumulado = acumulado + nota_actual
print(f"El promedio es {acumulado/10}")