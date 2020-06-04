#Desafio  - Perguntar até receber resposta válida

sexo =''

while sexo != 'M' and sexo != 'F' :
    if sexo == '':
        sexo = input('Digite seu sexo [M/F]: ')
    else:
        print('Resposta invalida! Digite novamente')
        sexo = input('Digite seu sexo [M/F]: ')
