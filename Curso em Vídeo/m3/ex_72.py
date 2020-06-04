#Desafio - Digitar um número entre 0 e 20 e printar o número por extenso

zero_vinte = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quize','dezesseis','dezesete','dezoio','dezenove','vinte')
numero = -1
while numero <0 or numero >20:
    numero=int(input('Digite um número de 0 a 20 para printar por extenso: \n'))

print(f'Você digitou o número {zero_vinte[numero]}')