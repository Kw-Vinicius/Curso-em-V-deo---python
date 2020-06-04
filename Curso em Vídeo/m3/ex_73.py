# Desafio - Times do Campeonato Brasileiro
# 5 primeiros colocados
# 4 ultimos colocados
# Times em ordem alfabética
# Colocação do time "Palmeiras"

times = ('Atlético-MG','Fortaleza','Coritiba','São Paulo','Flamengo','Botafogo','Sport Recife','Internacional',
         'Fluminense','Ceará SC','Goiás','Bragantino','Athletico','Grêmio','Bahia','Palmeiras','Corinthias','Vasco da Gama','Santos','Atlético')

print(f'Os 5 primeiros colocados são {times[:6]}')
print(f'Os ultimos 4 colocados são {times[-4:]}')  #Funcionaria também times[16:] mas não seria genérico para uma tupla que não se conhece o tamanho
print(f'Times em ordem alfabética: \n')
print(f'{sorted(times)}')
print(f'O palmeiras está na colocação: {times.index("Palmeiras")}')
