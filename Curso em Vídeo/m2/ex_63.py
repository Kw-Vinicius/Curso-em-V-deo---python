# Sequência de Fibonacci

fibonacci = int(input('Digite quantos números deseja ver da sequência de fibonacci: '))
cont = 0
numero1 = 0
numero2 = 1
while cont != fibonacci:
    cont += 1
    auxiliar = numero1
    print(f'{numero1}')
    numero1 = numero2
    numero2 = auxiliar+numero2