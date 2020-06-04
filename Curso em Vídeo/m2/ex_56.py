# Registro de pessoas

quantidade = int(input('Quantas pessoas deseja registrar? '))

media = 0
menos_de_vinte = 0
maior_idade=0
mais_velho=''

for quantia in range(0,quantidade+1):

    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ').strip().lower()
    idade = int(input('Digite sua idade: '))

    if quantia == 0:
        if sexo == 'masculino':
            maior_idade = idade

    media += idade
    if sexo == 'masculino':
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome

    if sexo == 'feminino':
        if idade < 20:
            menos_de_vinte += 1

print(f'O número de mulheres com menos de 20 anos é {menos_de_vinte}')
print(f'O nome do homem mais velho é {mais_velho}')
print(f'A media de idade das pessoas registradas é : {media/quantidade}')
