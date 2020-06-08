# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

op=''
lista=[]
lista_par=[]
lista_impar=[]

while op != 'n':
    lista.append(int(input('Digite um valor: ')))
    op = input('Deseja adicionar mais um numero na lista: [s] / [n] ')

for aux in range(0,len(lista)):
    if lista[aux] % 2 == 0:
        lista_par.append(lista[aux])
    else:
        lista_impar.append((lista[aux]))

print(lista)

print('Lista par:')
print(lista_par)

print('Lista impar: ')
print(lista_impar)