# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiores = 0
menores = 0
atual =date.today().year

for idades in range(0,7):
    ano=int(input('Ano de nascimento: '))
    if atual - ano <18:
        menores +=1
    else:
        maiores +=1

print(f'Maiores de idade: {maiores}')
print(f'Menores de idade: {menores}')
