# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    ficha.append([nome,[nota1 , nota2],media])
    opcao = str(input('Quer continuar? [s] / [n] ')).lower()

    if opcao == 'n':
        break

print('-'*30)
print(f'| {"No.":<4}| {"Nome":<10}| {"Media":>8} |')
print('-'*30)
for i,a in enumerate(ficha):
    print(f'| {i:<4}| {a[0]:<10}| {a[2]:>8} |')

print('-'*30)

while True:
    op = int(input('Quer ver a nota de qual aluno? (999 interrompe) '))
    if op == 999:
        break
    while op >= len(ficha):
        print('Digite um valor valido!!')
        op = int(input('Quer ver a nota de qual aluno? (999 interrompe) '))

    print(f'O aluno {ficha[op][0]} tirou as notas: {ficha[op][1]}')
    print('-' * 30)