# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dicionario = {}
dicionario['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = datetime.now().year - nascimento
dicionario['ctps'] = int(input('Carteira de trabalho ( 0 não tem): '))
if dicionario['ctps'] != 0:
    dicionario['contratação'] = int(input('Digite o ano de contratação: '))
    dicionario['salario'] = float(input('Digite seu salário: R$'))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - datetime.now().year)

for k,v in dicionario.items():
    print(f'{k} tem valor {v}')