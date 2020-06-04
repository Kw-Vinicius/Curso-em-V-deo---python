# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').upper().strip()  #Deixando a frase toda maiuscula e eliminando espaços antes e depois da frase
palavras = frase.split()   #Separando cada palavra da frase
junto = ''.join(palavras)  #Variavel junto recebe as palavras soltas e juntas elas sem espaço nenhum
invertida = ''             #Variavel invertida é uma string vazia q recebe a frase de trás p/ frente

for letra in range(len(junto)-1,-1,-1):    #Inicia a contagem no tamanho da string -1, faz a leitura até o inicio da frase, conta de trás p/ frente -1
    invertida += junto[letra]              #String vazia invertida recebe letra por letra da frase de trás p/ frente

if invertida == junto:                     #Se a string invertida for igual a string normal então temos um caso de palindromo
    print('É palindromo')
else:
    print('Não é palindromo')

