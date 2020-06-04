# Desafio Seis números inteiros, soma dos pares


somador = 0

for contador in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if(n % 2 ==0):
        somador += n

print(f'A soma dos números pares digitados é {somador}')