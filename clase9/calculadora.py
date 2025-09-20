"""
Crear un programa que dados 
dos valores
numericos, realice las 4 
operaciones basicas, usando
funciones para cada una de ellas

El programa debe funcionar de 
dos formas:

1. Pidiendo los datos a 
traves de consola
2. Pidiendo los datos a 
traves de linea de comandos

Ejemplos:
python calculadora.py debe pedir por consola
python calculadora.py 10 5 -> 
"""
import sys

def sumar(a, b):
    return a + b

def resta(a,b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

if len(sys.argv) > 1:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
else:
    num1 = float(input("Ingrese el primer numero \n"))
    num2 = float(input("Ingrese el segundo numero \n"))

print("suma " + str(sumar(num1, num2)))
print("resta " + str(resta(num1, num2)))
print("multiplicacion " + str(multi(num1, num2)))
print("division " + str(div(num1, num2)))