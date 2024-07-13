#!/usr/bin/env python

""" Calcula o bônus anual total de um funcionário """
__version__ = "0.3.0"
__author__ = "Tiago Fialho"

import sys

BONUS_BASE = 1000.00
nome_valido = False
salario_valido = False
bonus_valido = False


while not nome_valido:
    try:
        nome_funcionario = input("Informe o nome do funcionário: ")
        nome_funcionario = nome_funcionario.strip()
        # verifica se o nome está vazio
        if len(nome_funcionario) == 0:
            raise ValueError("O nome do funcionário deve ser digitado!")
        # verifica se há números no nome
        elif any(char.isdigit() for char in nome_funcionario):
            raise ValueError("O nome não deve conter números")
        else:
            print(f"{nome_funcionario} é um nome válido")
            nome_valido = True
    except ValueError as e:
        print(e)

# verifica se o salario é maior que zero e flutuante

while not salario_valido:
    try:
        salario = float(input(f"Salário do funcionário {nome_funcionario}: "))
        if salario <= 0:
            raise ValueError("Salário menor ou igual a zero")
        if not isinstance(salario, float):
            raise ValueError("O valor deve ser numérico")
        else:
            salario_valido = True
    except ValueError as e:
        print(e)

# verifica se o bonus é igual o maior que zero
while not bonus_valido:
    try:
        percentual_bonus = float(input(f"Percentual do bônus: "))
        if percentual_bonus < 0:
            raise ValueError("O bônus variável dever ser positivo ou igual a zero")
        else:
            bonus_valido = True
    except ValueError as e:
        print(e)
    

kpi = BONUS_BASE + (salario * percentual_bonus)

print("Cálculo do bônus anual: Bônus fixo + salario * percentual.")
print(f"O bônus anual total do funcionário {nome_funcionario} é de R$ {round(kpi, 2)}")
