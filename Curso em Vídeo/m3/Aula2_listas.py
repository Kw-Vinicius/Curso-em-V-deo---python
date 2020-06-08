galera = [['Vinicius',19],['Larissa',21],['Ana',20]]

print('= ' * 30)

print(galera)           # Printa tudo
print(galera[0])        #Printa somente o ['Vinicius',19]
print(galera[0][0])     #Printa somente o Vinicius
print(galera[1][1])     #Printa a idade de Larissa  = 21

print('= ' * 30)

for p in galera:
    print(p)            #Printa um por um da lista

print('= '*30)

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print('= '*30)

turma = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])             # Recebe só uma cópia dos valores
    dado.clear()

print(turma)

for p in turma:
    if p[1] >= 18:                            # Testando o indice correspondente a idade de cada pessoa
        print(f'{p[0]} é maior de idade.')    # Pegando o indice correspondente aos nomes
    else:
        print(f'{p[0]} é menor de idade.')    # Pegando o indice correspondente aos nomes

print('= '*30)