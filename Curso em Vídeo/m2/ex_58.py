# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n_random = randint(1,5)
numero = -1

while numero != n_random:
    if numero == -1:
        numero = int(input('Digite um número de 1 a 5: '))
    else:
        print('Você errou o número gerado! Tente novamente: ')
        numero = int(input('Digite um número de 1 a 5: '))

print(f'Você acertou, o número era : {n_random}')