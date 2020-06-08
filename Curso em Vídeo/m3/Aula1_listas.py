num = [2,5,1,9,1]       # Uso de [] para representar listas
num[2]=3                # A casa de endereço [2] recebe o valor 3
num.append(7)           # Adiciona mais uma casa no final da lista, colocando o valor 7 no novo endereço
num.sort                # Ordena de forma crescente
num.sort(reverse=True)  # Ordena de forma descrescente
num.insert(2,-1)        # Adiciona o numero -1 no endereço [2] e empurra o restante da lista um endereço p/ frente
num.pop(2)              # Remove o endereço [2] atual, concatenando o restante da lista
num.remove(9)           # Remove o primeiro número 9 que encontrar ( esquerda -> direita )
                        # Caso não exista um número 9, retorna erro

if 9 in num:
    num.remove(9)       # Evita o erro caso não encontre o 9

print(num)

valores = []

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))   # Adiciona elementos no final da lista dentro do loop

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

a = [2,3,4,7]
b = a[:]                 # Cria uma copia da lista a dentro da lista b
print(b)                 # Printa a lista a

b = a                    # As listas 'a' e 'b' foram conectadas, alterar uma influencia na outra

b[1] = 8                 # a[1] = b[1] = 8
print(a[1])              # Vai printar 8



