import sys

#Crear un programa que sume dos numeros

#Aca se pide por consola al usuario
#n1 = float(input("Ingrese el primer numero \n"))
#n2 = float(input("Ingrese el segundo numero \n"))

#El primer argumento osea el indice 0 siempre es el nombre del archivo
nombre_archivo = sys.argv[0]
print(nombre_archivo)

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])

print("El resultado es " + str(n1 + n2))