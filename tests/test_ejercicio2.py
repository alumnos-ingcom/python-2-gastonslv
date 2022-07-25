################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import estadistica

"""
En este test se estará probando los posibles caminos para la
función de estadística. El objetivo es ejercitar todos los caminos
del algoritmo.
"""


def test_estadistica_1():
    """
    En esta funcion ejercitamos las primeras tres estructuras
    condicionales if, finalizando el programa sin pasar por el while.
    """
    secuencia = (5,6)
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado no es tuple."
    assert resultado == (6,5,5.5), "Resultado no esperado." #(mayor,menor,promedio)
    
def test_estadistica_2():
    """
    En esta función ejercitamos la primera estructura condicional repetitiva,
    donde dentro tiene dos estructuras condicionales que también se
    ejercitarán, finalizando el programa.
    """
    secuencia = (1,2,3,4)
    resultado = estadistica(secuencia)
    assert isinstance(resultado, tuple), "El resultado no es tuple."
    assert resultado == (4,1,2.5), "Resultado no esperado."
