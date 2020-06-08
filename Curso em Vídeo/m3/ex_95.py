# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    total_partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    partidas.clear()
    for cont in range(0,total_partidas):
        partidas.append(int(input(f'Quantos gols foram feitos na partida {cont+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())    # Jogador é um dicionário , usar .copy
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if(resp in'SN'):
            break
        print('Erro! Responda apenas S ou N')
    if resp == 'N':
        break


print('='*50)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()

print('='*50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]['gols']):
            print(f' No jogo {i} fez {g} gols')