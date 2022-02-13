# Separando dígitos de um número
'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados
Ex: número: 1835; unidade: 4, dezena: 3, centena: 8, milhar: 1'''

n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('\033[37m''Analisando o número {}...\033[m'.format(n))
print('\033[1m''Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
