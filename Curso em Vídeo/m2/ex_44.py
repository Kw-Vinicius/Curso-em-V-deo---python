# Desafio
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preço = float(input('Digite o preço do produto: R$'))

print('Opções de pagamento:')
print('[1] À vista (dinheiro/cheque) , 10% de desconto')
print('[2] À vista no cartão, 5% de desconto')
print('[3] Em até 2x no cartão, preço normal')
print('[4] 3x ou mais no cartão, 20% de juros')

opção = int(input('Digite sua escolha: '))

if opção == 1:
    print(f'Pagamento à vista, valor cobrado : R${preço - (preço*0.1)}')
elif opção ==2:
    print(f'Pagamento à vista no cartão, valor cobrado :R${preço - (preço*0.05)}')
elif opção ==3:
    print(f'Pagamento em até 2x no cartão, valor cobrado: R${preço}')
elif opção ==4:
    print(f'Pagamento em até 3x ou mais no cartão, valor cobrado: R${preço + (preço*0.2)}')