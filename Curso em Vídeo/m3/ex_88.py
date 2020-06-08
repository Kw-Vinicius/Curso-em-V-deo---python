# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogos = list()
cont = 0
quantidade = int(input('Quantos jogos deseja jogar? '))

for x in range(0,quantidade):
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    cont = 0
    lista.clear()


for c in range (0,len(jogos)):
    print(f'O jogo {c+1} sorteado foi: {jogos[c]}')