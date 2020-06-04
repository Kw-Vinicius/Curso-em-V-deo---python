# Desafio
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Amora','Cobertor','Esquilo','Rio','Montanha')

for aux in palavras:
    print(f'\n palavra {aux} possui as vogais: ', end='')
    for letra in aux:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')