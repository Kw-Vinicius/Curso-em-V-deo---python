#  Crie um programa onde o usuário digite uma expressão matematica qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está fechando todos os parênteses abertos anteriormente.

exp = str(input('Digite uma expressao matematica:  '))
pilha = []

for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressao está errada!')