# Fatorial

fatorial = int(input('Digite um número para saber seu fatorial: '))
acumula = 1
n=1

while n <= fatorial:
    acumula = acumula*n
    n += 1

print(f'O valor do fatorial de {fatorial} é : {acumula}')