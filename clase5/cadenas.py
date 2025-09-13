# Concatenar
hola = "Hola"
nombre = input("Cual es tu nombre? \n") #\n es una secuencia de escape que representa un Enter 
saludo_completo = hola + " " + nombre
print(saludo_completo)
edad = int(input("Ingresa tu edad \n"))
print(nombre + " tu edad es " + str(edad))
# Convertir a mayusculas
saludo_en_mayus = saludo_completo.upper()
print(saludo_en_mayus)
# Convertir a minusculas
saludo_en_minus = saludo_completo.lower()
print(saludo_en_minus)
# Longitud de un texto
print ( "El saludo completo tiene una longitud de " + str(len(saludo_en_minus)) )
# Repeticiones
print( (saludo_completo + "\n") * 3)

# Acceso a caracteres
print(saludo_completo[0])

# Subcadena 
print (saludo_completo[0:6] )

# Dividir 0  1   2    3     4
cadena = "30,50,Hola,Juan,Pedro"
cadena_separada = cadena.split(",")
print(cadena_separada[3])