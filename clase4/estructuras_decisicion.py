condicion_igualdad = (10 == 10) # un simbolo igual = sirve para asignar, dos simbolos para comparar
desigualdad = (10 != 10)
comparacion_mayor = (11 > 10)
comparacion_menor = (10 < 11)
comparacion_mayor_igual = (11>= 10)
comparacion_menor_igual = (10 <= 11)

"""
Escribir un programa que dada la edad determine si
una persona es mayor de edad.

Entradas: 
Edad como Entero

Salida:
Es mayor o Es menor

Tabla de verificacion:
Entrada    Salida
17         Es menor
18         Es mayor
"""

print("Ingrese la edad")
edad_en_texto = input()
edad = int(edad_en_texto) #Convertimos a entero
if edad <=17:
    print("Es menor")
else:
    print("Es mayor")