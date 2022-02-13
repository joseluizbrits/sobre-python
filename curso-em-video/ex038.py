# Comparando números
'''Escreva um programa que leia DOIS NÚMEROS
inteiros e compare-os, mostrando na tela uma mensagem:
- O PRIMEIRO VALOR é MAIOR
- O SEGUNDO VALOR é MAIOR
- NÃO EXISTE valor maior, os dois são IGUAIS'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
if n1 > n2:
    print('O número {} é maior do que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior do que o número {}'.format(n2, n1))
else:
    print('\033[31m''Os números que você digitou são iguais')
