#! /usr/bin/env python
""" Calculadora de quatro operações"""
__version__ = "0.1.0"
__author__ = "Tiago Fialho"

import sys

try:
    valor1 = float(input("Digite o primeiro valor: "))
except ValueError:
    print("Digite apenas números")
    sys.exit(1)

try:
    valor2 = float(input("Digite o segundo valor: "))
except ValueError:
    print("Digite apenas números")
    sys.exit(1)

try:    
    operador = input("Informe a operação desejada (+, -, *, /): ")
except ValueError:
    print("Digite apenas os simbolos")
    sys.exit(1)

if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    try:
        resultado = valor1 / valor2
    except ZeroDivisionError:
        print("Divisão por ZERO não é uma operação válida")
        sys.exit(1)
else:
    print("Os operadores disponíveis são +, -, *, /")

print("Resultado: ", resultado)


