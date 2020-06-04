# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Digite 999 para parar a soma!!!')
flag = 999
num = int(input('Digit um número: '))
soma = num

while True:
    num = int(input('Digit um número: '))
    if num == 999:
        break
    else:
        soma = soma + num

print(f'A soma de todos os números digitados foi {soma}')