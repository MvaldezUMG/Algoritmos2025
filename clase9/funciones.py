
# La funcion puede recibir o no parametros
def sumar(numero_1 : float, numero_2 : float):
    resultado = numero_1 + numero_2
    #la funcion puede devolver o no valores
    return resultado

def saludar(nombre):
    print("hola " + nombre)

suma = sumar(10, 30)
print(suma)
suma2 = sumar(40,50)
print(suma2)

saludar("Marco")
suma3 = sumar(20,50)
print(suma3)

#funcion con parametros indefinidos
def imprimir_valores(*args):
    for valor in args:
        print(valor)

imprimir_valores("hola", 1, "JO", False)

def sumar_indefinido(*args : float):
    total = 0
    for valor in args:
        total = total + valor
    return total

suma_con_multiples_valores = sumar_indefinido(1,54,7.4,8,3,5,5,8)
print(suma_con_multiples_valores)

def devolver_multiples_valores():
    return 1, "Hola"

valores = devolver_multiples_valores()
print(valores)