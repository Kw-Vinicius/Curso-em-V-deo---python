#Desafio - Receber quatro valores pelo teclado preenchendo a tupla
# Quais numeros são pares?
# Quantos número 9 aparecem ?
# Onde apareceu o número 3?

TPL = (int(input('Digite o 1º valor: ')),
       int(input('Digite o 2º valor: ')),
       int(input('Digite o 3º valor: ')),
       int(input('Digite o 4º valor: ')))

print(TPL)
print(f'O número 9 apareceu {TPL.count(9)} vezes')
print(f'O número 3 apareceu pela primeira vez em {TPL.index(3)}')

print('Os números pares da tupla são:')
for aux in TPL:
    if aux %2 ==0:
        print(aux)