# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

n_inicial = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

aux = 0

while aux != 10:
    print(f'{n_inicial}')
    n_inicial = n_inicial + razao
    aux = aux+1

escolha = 'S'
aux = 0
while escolha == 'S' and escolha != 'N':
    escolha = input('Deseja ver mais valores da pa? [S/N]').upper().strip()
    if escolha == 'S':
        quantidade = int(input('Digite quantos valores a mais deseja ver: '))
        aux = 0
        while aux != quantidade:
            print(f'{n_inicial}')
            n_inicial = n_inicial + razao
            aux = aux + 1
