# Desafio
# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro : '))
print('[1] Para conversão binária')
print('[2] Para conversão octal')
print('[3] Para conversão hexadecimal')

escolha = int(input('Sua opção : '))

if escolha == 1:
    print(f'O número {numero} em conversão binária é : {bin(numero)}')
elif escolha == 2:
    print(f'O número {numero} em conversão octal é: {oct(numero)}')
elif escolha == 3:
    print(f'O número {numero} em conversão hexadecimal é {hex(numero)}')
else:
    print('Opção invalida!')