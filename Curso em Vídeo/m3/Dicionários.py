 # Tuplas ( )
 # Listas [ ]
 # Dicionários { }

filmes = {
     'titulo':'Star wars',
     'ano':1977,
     'Diretor':'George lucas'}

print(filmes)  # Printa {'titulo': 'Star wars', 'ano': 1977, 'Diretor': 'George lucas'}
print(filmes['titulo'])  # Star wars

print(f'O filme {filmes["titulo"]} foi lançado em {filmes["ano"]}')     # O filme Star wars foi lançado em 1977
 # OBS:  dentro do [] é necessário aspas duplas

print(filmes.keys())    # dict_keys(['titulo', 'ano', 'Diretor'])

print(filmes.values())  # dict_values(['Star wars', 1977, 'George lucas'])

print(filmes.items())   # dict_items([('titulo', 'Star wars'), ('ano', 1977), ('Diretor', 'George lucas')])

for k,v in filmes.items():   # titulo = Star wars
    print(f'{k} = {v}')      # ano = 1977
                             # Diretor = George lucas

# OBS: dicionário não usa o enumerate()

del filmes['ano']        # Apaga a key ['ano']

print(filmes.items())    # dict_items([('titulo', 'Star wars'), ('Diretor', 'George lucas')])

filmes['titulo'] = 'Star Wars : Clone wars'

print(filmes['titulo'])  # O nome foi alterado para: Star Wars : Clone wars

filmes['ano'] = 1977     # A key ano foi adicionada ao final do dicionário

print(filmes.items())    # dict_items([('titulo', 'Star Wars : Clone wars'), ('Diretor', 'George lucas'), ('ano', 1977)])

# -------------------------------------------------------------------------------------------------

print('-'*30)

brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)  # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
# OBS: brasil criou uma lista com 2 itens , sendo estado1 e estado2

print(brasil[0])  # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1])  # {'uf': 'São Paulo', 'sigla': 'SP'}

print(brasil[0]['sigla'])  # RJ
print(brasil[1]['uf'])     # São Paulo

# -------------------------------------------------------------------------------------------------

print('-'*30)

estado = dict()    # Outra forma de criar dicionários
br = list()        # A lista br também poderia ser criada como br =[]

for c in range(0,3):
    estado['uf'] = str(input('Digite a unidade federativa: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    br.append(estado.copy())                          # Dicionários não podem ser "fatiados", então não funciona o estado[:]
                                                          # Para isso o dicionário possui sua função própria xx.copy()
print(br)

for e in br:                                    # For para percorrer a lista
    for x,y in e.items():                       # For para percorrer o dicionário
        print(f'O campo {x} tem valor {y}')

# O campo uf tem valor Sao paulo
# O campo sigla tem valor sp
# O campo uf tem valor minas gerais
# O campo sigla tem valor mg
# O campo uf tem valor acre
# O campo sigla tem valor ac

for e in br:                        #
    for v in e.values():
        print(f'{v} ',end='')
    print()

# sao paulo sp
# Rio rj
# Acre ac 