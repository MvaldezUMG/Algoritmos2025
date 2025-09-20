"""
Crear un programa que permita realizar operaciones con estudiantes, 
los datos se deben guardar en un archivo de texto el cual se debe de
configurar desde el mismo menu.
con las siguientes caracteristicas:

Se debe almacenar los datos siguientes:
1. Nombre
2. Carnet
3. Carrera

1. Menu de opciones 
   - Configurar base de datos (archivo)
   - Crear estudiante
   - Listar estudiantes
   - Eliminar estudiante
   - Salir
"""
#Nombre del archivo donde se almacenan los datos
base_de_datos = ""

def configurar_base_de_datos():
    #Cuando queremos modificar una variable global hay que agregar la palabra clave.
    global base_de_datos    
    base_de_datos = input("Ingrese el nombre del archivo donde se guardan los datos\n")
    base_de_datos += ".txt"
    print("los datos se van a guardar en " + base_de_datos)

#configurar_base_de_datos()

def crear_estudiante():
    nombre = input("Ingrese el nombre\n")
    carnet = input("Ingrese el carnet\n")
    carrera = input("Ingrese la carrera\n")
    linea = nombre + "," + carnet + "," + carrera + "\n"
    #Abrimos el archivo en modo append (+a)
    archivo = open(base_de_datos, "+a")
    archivo.write(linea)
    archivo.close()

def listar_estudiantes():
    #Abro el archivo en modo lectura (+r)
    archivo = open(base_de_datos, "+r")
    lineas = archivo.readlines()
    #Cerramos el archivo
    archivo.close()
    for linea in lineas:
        datos = linea.split(",")
        print("Nombre:" + datos[0] + " Carnet: " + datos[1] + " Carrera:" + datos[2])

#crear_estudiante()
#listar_estudiantes()

def eliminar_estudiante(valor_buscado):
    #abrimos en modo lectura y escritura
    
    archivo = open(base_de_datos, "r+")
    lineas = archivo.readlines()
    encontrado = False
    indice_donde_esta = -1
    for indice, linea in enumerate(lineas):
        print("LINEA", linea)
        encontrado = valor_buscado in linea
        if encontrado:
            indice_donde_esta = indice

    if indice_donde_esta == -1:
        #Creamos un mensaje y hacemos un return para que el programa no continue.
        print("Estudiante no encontrado")
        return
    
    lineas[indice_donde_esta] = ""
    archivo.writelines(lineas)
    print("Estudiante borrado correctamente")
    archivo.close()

#eliminar_estudiante("Juan")

def menu():
    while True:
        print("Menu:")
        print("1. Configurar base de datos")
        print("2. Crear estudiante")
        print("3. Listar estudiantes")
        print("4. Eliminar estudiantes")
        print("5. Salir")

        opcion = int(input("Ingrese el numero de opcion\n"))
        if opcion == 1:
            configurar_base_de_datos()
        elif opcion == 2:
            if base_de_datos == "":
                print("La base de datos no ha sido configurada")
                continue
            crear_estudiante()
        elif opcion == 3:
            if base_de_datos == "":
                print("La base de datos no ha sido configurada")
                continue
            listar_estudiantes()
        elif opcion == 4:
            if base_de_datos == "":
                print("La base de datos no ha sido configurada")
                continue
            valor_buscado = input("Ingrese el nombre o carnet del estudiante\n")
            eliminar_estudiante(valor_buscado)
        elif opcion == 5:
            break

menu()
