# Números primos
'''Faça um programa que leia um NÚMERO INTEIRO
e diga se ele é ou não um NÚMERO PRIMO'''

n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1:33m''{}''\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m''{}''\033[m'.format(c), end=' ')
if cont == 2:
    print('\n\033[1m''O número {} é primo'.format(n))
else:
    print('\n\033[1m''O número {} não é primo'.format(n))
