# Cálculo do Fatorial
'''Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

from math import factorial
n = int(input('\033[1m''Digite um número para calcular o seu Fatorial: \033[m'))
f = factorial(n)
print('O fatorial de \033[1;35m{}\033[m é \033[1;35m{}\033[m.'.format(n, f))
