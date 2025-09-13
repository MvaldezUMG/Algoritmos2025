hola = "Hola"
mundo = "Mundo"
#Operaciones

#Concatenar 
hola_mundo = hola + " " + mundo
#Concatenar con otros tipos
numero = 10
hola_mundo = hola_mundo + str(numero)
print(hola_mundo)
#Acceder a un caracter a traves de su indice
print(hola[3])
#Accecer a un rango de caracteres
print(hola[0:3])
print(hola * 3)
#Reemplazar
print(hola_mundo.replace("Mundo", "Algoritmos B"))
#Buscar dentro del texto
texto_largo = "Hola estudiantes aplicados de Algoritmos"
indice = texto_largo.find("Juanito")
print(indice)
#Convertir a mayusculas
print(hola_mundo.upper())
#Convertir a minusculas
print(hola_mundo.lower())
#Convertir a primera mayuscula
print(hola_mundo.capitalize())
print(hola_mundo.capitalize())
#Dividir 
datos = "Nombre;Apellido;Nota\nJuan;Perez;10\nPedro;Martinez;9"
datos_separados = datos.split("\n")
#Acceder los datos de forma independiente
print(datos_separados[0])

datos_procesados = []
for linea in datos_separados:
    linea = linea.split(";")
    datos_procesados.append(linea)
print(datos_procesados)
print(datos_procesados[1][1])
print(datos_procesados[2][1])