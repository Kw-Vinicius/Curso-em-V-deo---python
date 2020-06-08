
lanche = ('Suco' , 'Hamburguer', 'Pizza' , 'Pudim')

print('=' *30)

print(lanche[1])    #Printa o conteudo do vetor no endereço 1 (hamburguer)
print(lanche[:2])   #Printa todas os conteudos de cada endereço até o 2 (exclui o 2)
print(lanche)       #Printa a tupla inteira
print(len(lanche))  #Printa 4, que corrensponde ao número de itens da tupla

# Lembrete : não é possível atribuir itens a tuplas, ex : ERRADO --> lanche[1] = bolo <-- ERRADO

print('=' *30)

for comida in lanche:
    print(f'Eu vou comer {comida}')   #Vai printar a frase para cada item da tupla

print('=' *30)

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')   #Vai printar a frase para cada item da tupla

print('=' *30)

for posicao, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {posicao} ')

print('=' *30)

print(sorted(lanche))  #Coloca em ordem a tupla (transforma em uma lista), perceba que no print a tupla aparece com []
print(lanche)          #Tupla representada com parenteses ()

print('=' *30)

tuplaX = (5,1,5,3,4,2)
tupla_a = (1,3,5)
tupla_b = (2,4,6)
tupla_c = tupla_a + tupla_b  #Concatena as tuplas resultando em (1,3,5,2,4,6)
print(tupla_c)
print(tupla_c.index(3))  #Mostra em qual index(enredeço) da tupla está o número 3 (está no index tupla_c[1])
print(tuplaX)
print(tuplaX.index(5,1)) #Mostra onde está o primeiro número 5 , começando a procurar a partir do endereço 1

tupla_mista = ('Larrisa',25,'F',1.68)   #tuplas podem conter vários tipos de variáveis diferentes
print(tupla_mista)
del(tupla_mista) #apaga a tupla, pode apagar qualquer variavel