#!/usr/bin/env python

""" Conversor de temperatura """
__version__ = "0.1.0"
__author__ = "Tiago Fialho"


try:  
    temperatura_celsius = float(input("Informe a temperatura em Celcius: "))
except ValueError:
    print("Temperatura deve ser um número")

try: 
    escala_para_conversao = input("Converter para Fahrenheit(F) ou Kelvin(K): ")
except ValueError:
    print("Digite F ou K")    
    
temperatura_convertida = "" 

if (escala_para_conversao.lower() == 'k'):
    temperatura_k = temperatura_celsius + 273
    temperatura_convertida = str(round(temperatura_k, 2)) + "K" 
elif (escala_para_conversao.lower() == 'f'):
    temperatura_f = (temperatura_celsius * 1.8) + 32
    temperatura_convertida = str(round(temperatura_f,2)) + "ºF"

print(f"{temperatura_celsius}º equivalem a {temperatura_convertida}")