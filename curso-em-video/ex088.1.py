# Palpites para a Mega Sena
'''Faça um programa que ajude um jogador da
MEGA SENA a criar PALPITES. O programa vai
perguntar QUANTOS JOGOS serão gerados e vai
sortear 6 NÚMEROS ENTRE 1 e 60 para cada jogo,
cadastrando tudo em uma LISTA COMPOSTA'''

from random import randint
from time import sleep
print('\033[1m''-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-''\033[m' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista = list()
print('-=' * 3, f' \033[1mSORTEANDO {jogos} JOGOS\033[m ', '-=' * 3)
for jogo in range(1, jogos + 1):
    for c in range(0, 6):
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        lista.sort()
    print(f'Jogo {jogo}: {lista}')
    lista.clear()
    sleep(1)
print('-=' * 5, '< \033[1mBOA SORTE!\033[m >', '-=' * 5)
