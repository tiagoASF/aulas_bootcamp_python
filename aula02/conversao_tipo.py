#! /usr/bin/env python

""" Conversão de tipo com validação """
__version__ = "0.1.0"
__author__ = "Tiago Fialho"

import sys

lista_numeros = input("Digite uma lista de números separados por vírgula: ")
numeros_str = lista_numeros.split(",")
numeros_int = []

for num in numeros_str:
    try:
        numeros_int.append(int(num.strip()))
    except ValueError:
        print("Os valores devem ser inteiros válidos")
        sys.exit(1)
print("Lista de inteiros: ", numeros_int)