# Respondendo ao usuário
'''Faça um programa que leia o nome de uma
pessoa e mostre uma mensagem de boas vindas'''

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}{}{}!'.format('\033[4m', nome, '\033[m'))
