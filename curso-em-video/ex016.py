# Quebrando um número
'''Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção inteira
Ex: O número 6,127 tem a parte inteira 6'''

from math import trunc
num = float(input('Digite um número qualquer: '))
print('O valor digitado foi \033[7;40m''{}\033[m e a sua porção inteira é \033[1;36m''{}'.format(num, trunc(num)))
