# def normalizar_nome(nome: str) -> str:
#     return nome.strip().lower()
def normalizar_nome(nome: str) -> str:
    return nome.strip().lower()

# nome = input("Informe o nome a ser normalizado: ")
# nome_normalizado = normalizar_nome(nome)
# print(nome_normalizado)

# nomes = [" Alice", "BOB", " Carlos  " ]
# # nomes_normalizados = []

# nomes_normalizados = [normalizar_nome(nome) for nome in nomes]
# print(nomes_normalizados)

# for nome in nomes:
#     nomes_normalizados.append(normalizar_nome(nome))

# print(nomes_normalizados)

### OPCAO
# nomes_normalizados = [normalizar_nome(nome) for nome em nomes]


# 01 - Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_numeros(numeros = []) -> int:
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# numeros = [10, 20, 300]
# soma_total = soma_numeros(numeros)
# print(soma_total)


# 02 - Crie uma função que receba um número como argumento e retorne True se o número for primo e
#False caso contrário.

# Um numero primo é aquele divisível por 1 e por ele mesmo

def is_primo(numero: int) -> bool:

    """Verifica se um número é primo.
        numero: número a ser testado
        saída: True para primo, False para não primo.

    """
    primo = True
    multiplos = []

    for valor in range(2, numero - 1): 
        multiplos.append(valor)
    
    for item in multiplos:
        if item % numero != 0:
            primo = False
            break

    return primo
        
    
# numero = int(input("Informe o número a ser testado: "))
# result = is_primo(numero)

# if (result):
#     print(f"{numero} é um número primo.")
# else:
#     print(f"{numero} não é primo.")

# print(is_primo.__doc__)

# 03 - Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.

def inverte_string(palavra: str) -> str:
    
    """Inverte uma string
    input: string a ser invertida
    output: string invertida
    """

    inverted_string = palavra[::-1]
    return inverted_string

# result = inverte_string("abacate")
# print(result)


# 04 - Implemente uma função que receba dois argumentos: uma lista de números e um número.
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# 05 - Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas


# DESAFIO - Exercicio KPi com dicionarios, type hint e funcoes
