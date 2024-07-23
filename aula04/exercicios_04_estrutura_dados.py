import math

# Exercicio 01 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros_auto = list(range(1, 11))

# for numero in numeros:
#     print(math.pow(numero, 2))

# Exercicio 02 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

languages = ["Python", "Java", "C++", "JavaScript"]
print(languages)
languages.remove("C++")
print(languages)
languages.append("Ruby")
print(languages)

# Exercicio 03 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

# Exercicio 04 - Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# Exercicio 05 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

# Exercicio 06 - Dada uma lista de emails, remover todos os duplicados.
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

# Exercicio 07 - Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# Exercicio 08 - Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# Exercicio 09 - Dado um conjunto de números, calcular a média.
# numeros = [10, 20, 30, 40, 50]

# Exercicio 10 - Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercicio 11 - Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# Exercicio 12 - Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# Exercicio 13 - Dado um dicionário, criar listas separadas para suas chaves e valores.
# dicionario = {"a": 1, "b": 2, "c": 3}

# Exercicio 14 - Dada uma string, contar a frequência de cada caractere usando um dicionário.
# texto = "engenharia de dados"
# frequencia = {}