# Desafio
# Analisando Triângulos

l1 = int(input('Digite a medida do 1º lado do triângulo: '))
l2 = int(input('Digite a medida do 2º lado do triângulo: '))
l3 = int(input('Digite a medida do 3º lado do triângulo: '))

if l1 != l2 and l1 != l3 and l2!=l3:
    print(f'Triângulo escaleno de lados : {l1}, {l2} e {l3}')
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1!= l2) or (l2 == l3 and l1 != l2):
    print(f'Triângulo isósceles de lados : {l1}, {l2} e {l3}')
else:
    print(f'Triângulo equilátero de lados : {l1}')