# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []

jogador['nome'] = str(input('Digite o nome do jogador: '))
total_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

for cont in range(0,total_partidas):
    partidas.append(int(input(f'Quantos gols foram feitos na partida {cont+1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v} ')

print('='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
print('='*30)

for i,v in enumerate(jogador['gols']):
    print(f'Na partida {i+1} o {jogador["nome"]} fez {v} gols')
print(f'No campeonato foram um total de {jogador["total"]} gols')
