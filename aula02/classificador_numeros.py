#! /usr/bin/env python

""" Exercicio CLASSIFICADOR DE NUMEROS

Aplicação que recebe um valor e informa se é positivo, negativo, zero, par ou impar.

"""

import sys

positivo_negativo = ""
par_impar = ""

try:
    valor = int(input("Informe o número a ser classificado: "))
except ValueError:
    print("Digite apenas números!")
    sys.exit(1)

if valor > 0:
    positivo_negativo = "Positivo"
elif valor < 0:
    positivo_negativo = "Negativo"
else:
    positivo_negativo = "Zero" 

if valor % 2 == 0:
    par_impar = "Par"
else:
    par_impar = "Impar"

print(f"{valor} é {positivo_negativo} e {par_impar}")
