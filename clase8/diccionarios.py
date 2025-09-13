#Repaso de clase anterior
#Lista es la implementacion del arreglo en Python
lista = [1, 2, 4,6,7]
lista_strings = ["Hoa", "mundo"]
print(lista[0])

#Estructuras de datos: Diccionarios
estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Ingenieria en sistemas",
    "cursos": ["Algebra lineal", "Algoritmos", "Matematica Discreta", "Contabilidad", "Precalculo"]
}

#Acceder a sus valores
print(estudiante["nombre"])
print(estudiante["edad"])
print(estudiante["carrera"])

for curso in estudiante["cursos"]:
    print(curso)

print(estudiante["cursos"][0])

#Acceder a una propiedad que no existe genera un error KeyError
#print(estudiante["CualquierCOSA"])
print(estudiante.get("CualquierCOSA", "este valor aparece si no existe el atributo"))

#Los diccionarios son mutables
estudiante["nombre"] = "Pedrito"
print(estudiante.get("nombre"))

#Podemos tratar las variables segun su tipo
print(len(estudiante["cursos"]))

diccionario_complejo = {
    "nombre": "Juan",
    "horario_cursos": {
        "Algebra lineal": "7AM",
        "Algoritmos": "9AM",
    }
}
print(diccionario_complejo["horario_cursos"]["Algebra lineal"])

# Obtener todas las llaves como lista
llaves_de_estudiante = estudiante.keys()
print(llaves_de_estudiante)

#Imprimir todos los valores y las llaves que tiene
for llave, valor in estudiante.items():
    print(llave + ":" + str(valor))

#Obtener los valores y convertir en una lista
valores_estudiante = estudiante.values()
print(list(valores_estudiante))

#Limpiar el contenido
estudiante.clear()
print(estudiante)

#Actualizar propiedades, pero elimina el resto
estudiante.update({
    "nombre": "Jose",
    "edad": 30,
    "otraPropiedad": "prueba"
})

print(estudiante)