# Tipos de datos sencillos
mi_numero = 5
print(mi_numero)

mi_numero = 10

#nombre = input("Ingrese su nombre \n")

#Lista de notas
notas = [10,15,20,6,12,5]

#acceder a un valor
print(notas[0])
print(notas[-6])

#Lista de nombres
nombres = ["Rocio", "Suarlin", "Genesis", "Brandon", "Pepe"]

#acceder a nombres por indice
print(nombres[2])

#Reemplazar valores
nombres[0] = "Carlos"

#Agregar otro nombre
nombres.append("Rosbelyn")

#Explorar todos los elementos
for nombre in nombres:
    print(nombre)

# Lista de listas
lista_de_grupos = [ ["Dany","Eddy"],["Ismael", "Gerson"], ["Ashly", "Sofia"] ]

#Reemplazar a Gerson por Brandon
lista_de_grupos[1][1] = "Brandon"

#Explorar lista de listas
for grupo in lista_de_grupos:
    for nombre in grupo:
        print(nombre)

#Buscar en una lista

#Busqueda tradicional usando for con enumeradori i
encontrado = -1
for indice, nombre in enumerate(nombres):
    if nombre == "Suarlin":
        encontrado = indice
print("Suarlin esta en la posicion " + str(encontrado))

#Funciones de listas de python
encontrado = nombres.index("Suarlin")
print("Suarlin esta en la posicion " + str(encontrado))

#Remover elementos
nombres.remove("Suarlin")
print(nombres)

#Insertar en una posicion especifica
nombres.insert(2, "Kevin")
print(nombres)

# Combinar listas con .extend
otros_nombres = ["Fatima", "Daniela"]
nombres.extend(otros_nombres)
print(nombres)

# Contar cuantos elementos hay en una lista
print(len(nombres))