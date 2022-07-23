################
# Gaston Silvestre - @gastonslv
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas

Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""

def estadistica(numero):
    """
    Esta funcion separa el número máximo, mínimo y el promedio de ambos de la
    secuencia de números que se ingresa.
    Como mínimo se deben ingresar dos números.
    """
    mayor = 0
    menor = 0
    lista = []
    tuple_ = 0
    indice = 0
    contador = len(numero)

    if numero[0] >= numero[1]:
        mayor = numero[0]
        menor = numero[1]

    if numero[1] >= numero[0]:
        mayor = numero[1]
        menor = numero[0]

    if contador > 2:
        indice = 2
        while contador != indice:
            if numero[indice] > mayor:
                mayor = numero[indice]
            if numero[indice] < menor:
                menor = numero[indice]
            indice += 1

    promedio = (mayor + menor) / 2

    lista.append(mayor)
    lista.append(menor)
    lista.append(promedio)

    tuple_ = tuple(lista)
    return tuple_

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = []
    bucle = True
    while bucle:
        try:
            decision_usuario = int(input("Cuántos numeros desea procesar?: "))
            if decision_usuario >= 0:
                bucle = False
        except ValueError:
            print("El valor ingresado es incorrecto,")
            print("vuelva a intentarlo.")

    while decision_usuario > 0:
        try:
            valor = int(input("Ingrese un valor para la secuencia de numeros: "))
            lista.append(valor)
            decision_usuario -= 1
        except ValueError:
            print("El valor ingresado es incorrecto,")
            print("vuelva a intentarlo.")
    resultado = estadistica(lista)
    print(resultado)

if __name__ == "__main__":
    principal()
