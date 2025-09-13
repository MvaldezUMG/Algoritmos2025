""" Crear un programa que permita traducir las palabras seleccionando el idioma de origen
y el idioma destino, por ejemplo:

ES-EN - Español - Ingles
EN-ES - Ingles - Español

"""
todas_las_traducciones = {
    "ES-EN": {
        "hola": "hi",
        "silla": "chair",
        "vaso": "glass",
        "puerta": "door",
        "mesa": "table"
    },
    "EN-ES": {
        "hi": "hola",
        "chair": "silla",
        "glass": "vaso",
        "door": "puerta",
        "table": "mesa"
    }
}

while True:
    traduccion = input("ingrese la traduccion deseada con los codigos como ES-EN o EN-ES\n")
    if traduccion == "0":
        break
    traducciones = todas_las_traducciones.get(traduccion)
    if traducciones == None:
        print("La traduccion no existe")
        continue
    while True:
        palabra = input("ingrese la palabra que desea traducir\n")
        if palabra == "0":
            break
        palabra_traducida = traducciones.get(palabra)
        if palabra_traducida == None:
            print("El diccionario no cuenta actualmente con una traduccion para "+ palabra_traducida)
        print("La palabra traducida es " + palabra_traducida)