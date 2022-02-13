# Cálculo do Fatorial
'''Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input('Digite um número: '))
fatorial = 1
c = 1
for c in range(1, n):
    fatorial *= (c + 1)
    c += 1
print('O fatorial do número \033[32m{}\033[m é igual a \033[32m{}'.format(n, fatorial))
