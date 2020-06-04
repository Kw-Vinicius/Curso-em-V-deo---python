# Desafio
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
tempo = int(input('Digite em quantos anos quer pagar a casa: '))
mensalidade = casa /(12*tempo)
if casa / (12*tempo) >= 0.3*salario:
    print(f'O valor cobrado mensalmente, R${mensalidade}  é superior a 30% do seu salário R${salario*0.3},financiamento negado!')
else:
    print('Financiamento aprovado!')