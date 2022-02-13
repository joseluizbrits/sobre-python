# Calculando Descontos
'''Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5% de desconto'''

p = float(input('\033[1;33mDigite o preço do produto: '))
px = p * 0.95
print('\033[1;33m''Em uma liguidação esse produto de \033[1;31mR$ {:.2f}\033[1;33m'.format(p), end=' ')
print('sairia por\033[m \033[1;30;42m''R$ {:.2f}\033[m'.format(px))
