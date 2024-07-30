import csv

path = 'exemplo.csv'
data_from_csv = []

with open(path, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        data_from_csv.append(linha)

for register in data_from_csv:
    print(register)
