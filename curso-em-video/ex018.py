# Seno, Cosseno e Tangente
'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
cor = {'verde': '\033[32m',
       'limpa': '\033[m'}
print('O ângulo de {}{:.0f}°{} tem:'.format(cor['verde'], ang, cor['limpa']))
print('SENO = {}{:.2f}{}'.format(cor['verde'], sin, cor['limpa']))
print('COSSENO = {}{:.2f}{}'.format(cor['verde'], cos, cor['limpa']))
print('TANGENTE = {}{:.2f}{}'.format(cor['verde'], tan, cor['limpa']))
