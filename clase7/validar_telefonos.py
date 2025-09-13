"""
Escriba un programa que dados N cantidad de numeros de telefono,
genere una lista guardando los que son validos y otra con los invalidos.

El formato de un telefono en Guatemala es el siguiente: 
+502 4040-4030

Ejemplo:
Entradas         Salidas
+502 3920-3923   Valido
+502 39392923    Invalido
3934-9439        Invalido
22139392         Invalido
"""
validos = []
invalidos = []
while True:
    telefono = input("Ingrese el numero\n")
    if telefono == "salir":
        break
    if telefono.find("+502 ") > -1 and telefono.find("-") == 9:
        validos.append(telefono)
    else:
        invalidos.append(telefono)
    
print("validos")
print(validos)
print("Invalidos")
print(invalidos)