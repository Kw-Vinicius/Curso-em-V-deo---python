#Desafio - Preencher tupla aleatóriamente e printar maior e menor valores

import random

tupla = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(tupla)
print(f'O maior valor da tupla é {max(tupla)}')
print(f'O menor valor da tupla é {min(tupla)}')
