# Cálculo do Fatorial
'''Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input('\033[1m''Digite um número para calcular o seu Fatorial: \033[m'))
c = n
f = 1
print('\033[1m''Calculando \033[35m''{}!''\033[m = \033[m'.format(n), end='')
while c > 0:
    print('\033[1;33m''{}''\033[m'.format(c), end='')
    print(' x ' if c > 1 else '\033[1m = ', end='')
    f *= c
    c -= 1
print('\033[1;35m{}'.format(f))
