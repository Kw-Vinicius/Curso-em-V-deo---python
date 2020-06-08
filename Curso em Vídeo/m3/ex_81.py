# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

op=''
lista=[]
cont = 0

while op != 'n':
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    op = input('Deseja adicionar mais um numero na lista: ')


print(f'A quantidade de valores digitados foi: {cont}')
print('Lista ordenada de forma decrescente: ')
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('Existe o valor 5 na lista')
else:
    print('Não exite o valor 5 na lista')

