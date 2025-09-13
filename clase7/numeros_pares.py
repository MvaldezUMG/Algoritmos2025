'''
Crear un programa que dado N cantidad de numeros,
cree una lista nueva con los que son pares

Entradas:
N cantidad de numeros

Salidas:
Arreglo con numeros pares.

'''

numeros_pares = []
numeros_impares = []
while True:
    numero =  int(input("ingrese el numero\n"))
    if numero == -1:
        # Condicion de salida
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Pares")
for numero in numeros_pares:
    print(numero)
print("Impares")
for numero in numeros_impares:
    print(numero)