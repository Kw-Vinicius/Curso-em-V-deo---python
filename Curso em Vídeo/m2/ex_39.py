# Desafio
#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input('Digite o ano de nascimento: '))
atual = int(input('Digite o ano atual: '))

if atual - nascimento <18:
    print(f'Você ainda deve se alistar futuramente, tempo até alistamento : {atual - nascimento} anos')
elif atual - nascimento >18:
    print(f'Você passou do prazo de alistamento, tempo ultrapassado: {atual - nascimento} anos')
elif atual - nascimento == 0:
    print('Você deve se alistar este ano')