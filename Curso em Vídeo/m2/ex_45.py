# Desafio
#  Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('pedra','papel','tesoura')
aleatório = randint(0,2)
print("Escolha pedra , papel ou tesoura: [0] [1] [2]")
jogada = int(input('Digite sua escolha: '))

print(f'O computador jogou {itens[aleatório]}')
print(f'Você escolheu {itens[jogada]}')

if aleatório == 0 and jogada == 2:
    print("Você perdeu!")
elif aleatório == 0 and jogada == 1:
    print("Você ganhou!")
elif aleatório == 0 and jogada == 0:
    print("Empate!")
elif aleatório == 1 and jogada == 2:
    print("Você ganhou!")
elif aleatório == 1 and jogada == 1:
    print("Empate!")
elif aleatório == 1 and jogada == 0:
    print("Você perdeu!")
elif aleatório == 2 and jogada == 2:
    print("Empate!")
elif aleatório == 2 and jogada == 1:
    print("Você perdeu!")
elif aleatório == 2 and jogada == 0:
    print("Você ganhou!")