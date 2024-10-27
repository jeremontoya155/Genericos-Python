# import
# From import
import pandas as pandas
from algoritmosOrden import *
from request import *


class Generica():
    def __init__(self, nombre):
        self, nombre = nombre

    def datos(self):
        return f"Generico {self.nombre}"


def function1():
    datos_web("https://jsonplaceholder.typicode.com/posts/1")
    pass


def function2():
    pass


def functio3():
    pass


def function4():
    pass


def function5():
    pass


def separador():
    print(f"\n------------------------------------------------------\n")


if __name__ == "__main__":

    lista = [20, 564, 8, 4, 9494, 874, 88, 448, 8848, 5454, 5]
    separador()
    lista = quicksort(lista)
    print(lista)
    function1()
    function1()
    function1()
    function1()
    function1()
