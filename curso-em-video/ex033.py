# Maior e menor valores
'''Faça um programa que leia três números
e mostre qual é o MAIOR e qual é o MENOR'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
# Verificando qual número é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando qual número é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi \033[32m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[32m{}'.format(maior))
