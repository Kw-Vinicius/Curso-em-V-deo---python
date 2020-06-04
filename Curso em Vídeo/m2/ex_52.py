# Desafio - Número primo?

primo = int(input('Digite um número para saber se ele é primo: '))

auxiliar = 0

for contagem in range(1, primo+1):
    if primo % contagem == 0:
        auxiliar += 1

if auxiliar > 2:
    print(f'O número {primo} nao é primo!')
else:
    print(f'O número {primo} é primo!')