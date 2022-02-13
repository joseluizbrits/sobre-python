# Maior e menor valores em Tupla
'''Crie um programa que vai gerar CINCO
NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
Depois disso, mostre a LISTAGEM DE NÚMEROS
gerados e também indique o MENOR e o MAIOR
valor que estão na tupla'''

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi \033[1m{max(numeros)}\033[m') # comando max pega o maior valor em uma tupla
print(f'O menor valor sorteado foi \033[1m{min(numeros)}\033[m') # comando min pega o menor valor em uma tupla
