#!/usr/bin/env python

""" Verificador de palindromo """
__version__ = "0.1.0"
__author__ = "Tiago Fialho"


entrada = input("Informe uma frase ou palavra: ")
if isinstance(entrada, str):
    entrada_formatada = entrada.replace(" ", "").strip().lower()
    if entrada_formatada == entrada_formatada[::-1]:
        print(f"{entrada_formatada} --> É um palíndromo")
    else:
        print(f"{entrada_formatada} --> Não é um palíndromo")
else:
    print("Entrada inválida. Digite uma palavra ou frase.")

