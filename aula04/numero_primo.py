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
        
    
numero = int(input("Informe o número a ser testado: "))
result = is_primo(numero)

if (result):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é primo.")

print(is_primo.__doc__)