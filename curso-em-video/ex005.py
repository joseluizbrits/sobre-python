# Antecessor e Sucessor
'''Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor'''

n1 = int(input('Digite um número inteiro: '))
n0 = n1 - 1
n2 = n1 + 1
cor = {'limpa': '\033[m',
       'amarelo': '\033[0;33m',
       'roxona': '\033[0;35m'}
print('O antecessor deste número é {}{}{}'.format(cor['amarelo'], n0, cor['limpa']), end=' ')
print('e o sucessor é {}{}'.format(cor['roxona'], n2))
