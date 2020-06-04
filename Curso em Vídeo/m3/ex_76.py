# Desafio - Listagem de Preços
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

padaria = ('Pão',1.99,'Queijo',2.50,'Mortadela',2.00,'Café',3.50,'Chocolate',2.75,'Salgado',1.79)
print('='*15)
print('Padaria')
print('='*15)
for cont in range(0,len(padaria)):
    if cont % 2 ==0:
        print(f'{padaria[cont]:.<30} R${padaria[cont+1]:>5.2f}')
    cont = cont+1