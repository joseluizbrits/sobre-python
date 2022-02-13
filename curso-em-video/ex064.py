# Tratando vários valores v1.0
'''Crie um programa que leia VÁRIOS NÚMEROS
inteiros pelo teclado. O programa só vai parar
quando o usuário digitar 999, que é a CONDIÇÃO
DE PARADA. No final, mostre QUANTOS NÚMEROS foram
digitados e qual foi a SOMA entre eles'''
# DESCONSIDERANDO O FLAG, ou seja, o número 999

num = cont = soma = 0
num = int(input('Digite um número [999 para parar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar: '))
print('Você digitou \033[1:35m''{}''\033[m números e a soma entre eles foi \033[1:35m''{}''\033[m.'.format(cont, soma))
