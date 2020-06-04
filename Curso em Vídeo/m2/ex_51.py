#Desafio - Pa e Razão

primeiro = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))

for pa in range(primeiro,primeiro+(razao*10),razao):
    print(f'{pa}')