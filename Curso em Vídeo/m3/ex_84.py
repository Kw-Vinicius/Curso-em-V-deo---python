# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

temp = []
principal = []
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(float(input('Digite o peso da pessoa: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    principal.append(temp[:])
    temp.clear()

    op = str(input('Deseja cadastrar outra pessoa? [s] [n]'))
    if op in 'Nn':
        break


print('\n')
print(f'{len(principal)} Pessoas cadastradas')
print(f'O maior peso foi de {maior}Kg das pessoas : ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print('\n')
print(f'O menor peso foi de {menor}Kg das pessoas: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')
print('\n')