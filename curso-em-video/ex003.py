# Somando dois números
'''Crie um programa que leia dois número e mostre a soma entre eles'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s1 = n1 + n2
print('A soma entre ''\033[0;32m''{}''\033[m e \033[0;32m''{}''\033[m'. format(n1, n2), end=' ')
print('é \033[0;32m{}\033[m'.format(s1))
