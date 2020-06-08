#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


print('Digite um valor para adicionar na lista \nValores duplicados não são adicionados')

op=''
lista=[]

while op != 'n':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print(f'{valor} já existe na lista')
        op = input('Deseja adicionar outro valor? [s] / [n] : ').lower()
    else:
        lista.append(valor)

    op = input('Deseja adicionar outro valor? [s] / [n] : ').lower()

lista.sort()
print(lista)


