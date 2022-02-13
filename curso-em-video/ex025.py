# Procurando uma string dentro de outra
'''Crie um programa que leia o nome de uma
pessoa e diga se ela tem "SILVA" no nome'''

nome = str(input('\033[1m''Digite o seu nome:\033[m ')).strip()
print('\033[37m''Seu nome tem Silva?\033[m {}'.format('silva' in nome.lower()))
