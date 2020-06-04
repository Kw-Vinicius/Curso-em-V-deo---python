# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pesos in range(0,5):
    peso = int(input('Digite o seu peso(kg): '))
    if pesos == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso registrado foi : {maior}kg')
print(f'O menor peso registrado foi: {menor}kg')