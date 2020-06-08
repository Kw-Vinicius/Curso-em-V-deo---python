# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.


matriz = [[0,0,0],[0,0,0],[0,0,0]]

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite o valor da posição {c+1}x{l+1}: '))

for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]', end='')        # O :^5 serve para criar um espaçamento de 5 casas entre o proximo print da mesma linha
    print()   # Printa vazio só para pular linha, pois usando o \n criaria uma linha de espaçamento entre cada linha da matriz



