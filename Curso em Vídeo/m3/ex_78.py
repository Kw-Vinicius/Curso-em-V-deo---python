# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
menor = 0
maior = 0

for cont in range(0,5):
    lista.append(int(input('Digite um valor : ')))
    if cont == 0:
        maior = menor = lista[cont]
    if lista[cont] > maior:
        maior = lista[cont]
    if lista[cont] <menor:
        menor = lista[cont]

print(lista)

for x,aux in enumerate(lista):
    if aux == maior:
        print(f'O maior valor da lista é {maior} e sua posição é {x}')
    if aux == menor:
        print(f'O menor valor da lista é {menor} e sua posição é {x}')


