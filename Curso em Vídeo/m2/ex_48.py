# Soma de números impares multiplos de 3 no intervalo de 0 e 500

soma = 0;

for aux in range (0,500):
    if aux % 2 != 0 and aux % 3 == 0:
        soma += aux

print(f'A soma é {soma}')


