import sys
import time


### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


# dados_vendas = [(10,10), (1,5), (1000,34),(4,50),(55,50),(1,500),(2,25.50),(67,4),(9,3),(1,55),(1,23),(5,100.2),(-3,56.78),(2,1),(2,0.99)]

# dados_validos = True

# for venda in dados_vendas:
#     if venda[0] < 0 or venda[1] < 0:
#         dados_validos = False
        
# if dados_validos:
#     print("Dados de venda válidos")
# else:
#     print("Dados inválidos. Verifique os valores e quantidades lançados")



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# temperaturas_celcius = [10, 0, -20, -5, 1.45, 9, 79, 251, -0.01, 0, 55, 2, 4.5, 89]

# for temperatura in temperaturas_celcius:
#     if temperatura <= 5:
#         print(f"{temperatura}ºc: Baixa")
#     elif temperatura > 5 and temperatura < 35: 
#         print(f"{temperatura}ºc: Normal")
#     else:
#         print(f"{temperatura}ºc: Alta")




### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# logs = [
#         {'timestamp': '2021-06-23 10:00:00', 'level': 'NORMAL', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-23 10:00:00', 'level': 'NORMAL', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha no banco de dados'}
#     ]

# for log in logs:
#     if log.get('level') == 'ERROR':
#         print(f"Operação com falha crítica - {log.get('message')}")



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# nome_usuario = input("Informe o nome do usuário: ")
# email_usuario = input("E-mail: ")
# idade_usuario = int(input("Idade: "))

# if not (idade_usuario >= 18 and idade_usuario <= 65):
#     print(f"Usuário {nome_usuario} não cadastrado. Idade inválida")
#     sys.exit(1)
# else:
#     print("Data de nascimento válida. Próxima etapa, verificando e-mail...")

# if (("@" not in email_usuario) or ("." not in email_usuario)):
#     print("E-mail inválido")
#     print("Cadastro interrompido.")
#     sys.exit(1)
# else: 
#     print("E-mail válido. Cadastro completo!")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacoes = [
#     {'id': 1, 'valor': 12001, 'hora': 12},
#     {'id': 2, 'valor': 7000, 'hora': 14},
#     {'id': 3, 'valor': 6500, 'hora': 12},
#     {'id': 4, 'valor': 100, 'hora': 1},
#     {'id': 5, 'valor': 39000, 'hora': 20}
# ]

# for transacao in transacoes:
#     if transacao.get('valor') > 12000 or transacao.get('hora') > 18 or transacao.get('hora') < 9:
#         print(f"ALERTA: transação nº{transacao.get('id')} suspeita")
#         print(transacao)
# print("Analise completa")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = "O rato roeu a roupa do rei de Roma."
# texto = "Here what you learn in this tutorial: You cover the basic characteristics of Python dictionaries and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good sense of when a dictionary is the appropriate data type to use, and how to do so."

# palavras = texto.strip().split(" ")
# palavras_semanticas = []
# contador_de_palavras = {}

# for palavra in palavras:
#     if (len(palavra) >= 3):
#         palavras_semanticas.append(palavra)
# print(palavras_semanticas)

# for palavra in palavras_semanticas:
#     if palavra in contador_de_palavras:
#         contador_de_palavras[palavra] += 1
#     else:
#         contador_de_palavras[palavra] = 1

# print(contador_de_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
## (numero - minimo) / (max - minimo)

# numeros = [10, 20, 30, 40, 50, 60]
# numeros = [10, -2, 3, 330, 3, 6.0]
# numeros_normalizados = []
# min_numero = numeros[0]
# max_numero = numeros[0]

# for numero in numeros:
#     if numero > max_numero:
#         max_numero = numero
#     if numero < min_numero:
#         min_numero = numero

# for numero in numeros:
#     numeros_normalizados.append((numero - min_numero) / (max_numero - min_numero))

# print(numeros_normalizados)

## OUTRA RESOLUCAO
# min = min(numeros)
# max = max(numeros)
# normalizados = [((numero - min) / (max - min)) for numero in numeros]

# print(normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"},
#     {"nome": "", "email": "tiago@example.com"}
# ]

# usuarios_validos = []
# usuarios_invalidos = []

# for usuario in usuarios:
#     if usuario["email"] and usuario["nome"]:
#         usuarios_validos.append(usuario)
#     else:
#         usuarios_invalidos.append(usuario)

# print(usuarios_validos)
# print(usuarios_invalidos)




### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = [1, 20, 33, 40 -6, 0, 201, 20, 66, 15, 11]

# numeros_pares = []
# numeros_impares = []

# for numero in numeros:
#     if numero % 2 == 0:
#         numeros_pares.append(numero)
#     else:
#         numeros_impares.append(numero)

# print(numeros_pares)
# print(numeros_impares)



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de 
# vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800},
#     {"categoria": "livros", "valor": 100},
#     {"categoria": "livros", "valor": 50},
#     {"categoria": "livros", "valor": 10},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# vendas_por_categoria = {}

# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if (categoria in vendas_por_categoria):
#         vendas_por_categoria[categoria] += valor
#     else:
#         vendas_por_categoria[categoria] = valor

# print(vendas_por_categoria)



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# palavra = ""
# palavras_digitas = []

# while palavra != "sair":
#     palavra = input("insira uma palavra ('sair' para encerrar): " )
#     palavras_digitas.append(palavra)
    
# palavras_digitas.pop(-1)    
# print("Encerrando")
# print(palavras_digitas)


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# numero = None
# secrets = [1, 3, 4, 5, 6, 99]

# while numero not in secrets:
#     numero = int(input("Insira um valor inteiro: "))
#     print("Você errou!")

# print("Você acertou o segredo👌")



### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# pagina_atual = 1
# paginas_totais = 7

# while pagina_atual <= paginas_totais:
#     print(f"processando página {pagina_atual}...")
#     time.sleep(2)
#     pagina_atual += 1

# print("Páginas processadas")


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas_maximas = 5
# numero_tentativas = 1

# while numero_tentativas <= tentativas_maximas:
#     print(f"Tentativa {numero_tentativas}...")
#     numero_tentativas += 1
#     time.sleep(3)

# print("Tentativas excedidas. SYSTEM DOWN")    


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

dados = [1, 2, 3, 4, "stop", 5, 6, 7, 8, 9]

i = 0
while i < len(dados):
    if dados[i] == "stop":
        print("hora de parar")
        break
    print(f"processando item {i+1}") 
    i += 1