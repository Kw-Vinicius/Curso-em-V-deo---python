# Operações com 2 valores utilizando um menu

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = -1

print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior valor')
print('[4] Novos valores')
print('[5] Sair')

while opcao != 5:
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print(f'A soma dos valores {n1} e {n2} é : {n1+n2}')
    elif opcao ==2:
        print(f'A multiplicação dos valores {n1} e {n2} é: {n1*n2}')
    elif opcao == 3:
        if n1>n2:
            print(f'O maior valor é {n1}')
        elif n2>n1:
            print(f'O maior valor é {n2}')
        elif n2 == n1:
            print(f' Os dois valores são iguais {n1} e {n2}')
    elif opcao == 4:
        print('\n')
        n1 = int(input('Digite um novo valor para o primeiro número: '))
        n2 = int(input('Digite um novo valor para o segundo número: '))
