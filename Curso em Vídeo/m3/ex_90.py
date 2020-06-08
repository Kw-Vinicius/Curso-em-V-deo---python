# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.


aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] <5:
    aluno['situacao'] = 'Reprovado!'
else:
    aluno['situacao'] = 'Aprovado!'

print(aluno)

