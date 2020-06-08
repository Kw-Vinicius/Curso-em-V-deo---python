#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

pessoa = {}
lista = []
lista_mulher = []
lista_acima_media = []

while True:
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoa['sexo'] = str(input('Digite o sexo: [M] / [F] ')).lower()
    while True:
        if pessoa['sexo'] not in 'mf':
            print('Digite uma opção válida!')
            pessoa['sexo'] = str(input('Digite o sexo: [M] / [F] ')).lower()
        else:
            break

    lista.append(pessoa.copy())
    op =str(input('Deseja cadastrar outra pessoa? [s] / [n]  '))
    if op in 'nNnãoNão':
        break

print('='*30)
print(f'{len(lista)} pessoas foram cadastradas')
soma = 0
for c in range(0,len(lista)):
    soma += lista[c]['idade']
media = soma/len(lista)
print(f'A média de idade é {media:5.2f} anos')
print('='*30)

print('As mulheres cadastradas foram: ')
for p in lista:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}')

print('='*30)
print('Pessoas com a idade acima da média: ')
for p in lista:
    if p['idade'] > media:
        print(f'{p["nome"]}')

print('='*30)