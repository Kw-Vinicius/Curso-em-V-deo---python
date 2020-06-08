# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma_3c = 0
maior = 0

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite o valor da posição {c+1}x{l+1}: '))
        if matriz[c][l] % 2 == 0:
            soma += matriz[c][l]
        if l == 2:
            soma_3c += matriz[c][l]
        if c == 1 and maior < matriz[c][l]:
            maior = matriz[c][l]


for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]', end='')        # O :^5 serve para criar um espaçamento de 5 casas entre o proximo print da mesma linha
    print()   # Printa vazio só para pular linha, pois usando o \n criaria uma linha de espaçamento entre cada linha da matriz

print(f'A soma de todos os pares é : {soma}')
print(f'A soma dos elementos da 3 coluna é : {soma_3c}')
print(f'O maior elemento da 2 linha é :{maior}')