# Jogo da Adivinhação v.1.0
'''Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador "PENSAR"
print('\033[1:33m''-=-''\033[m' * 20)
print('\033[1:35m''Vou pensar em um número entre 0 e 5. Tente adinhar...''\033[m')
print('\033[1:33m''-=-''\033[m' * 20)
player = int(input('\033[1:35m''Em que número eu pensei? ')) # Jogador tenta adivinhar
if 0 <= player <= 5:
    print('\033[7:37m''PROCESSANDO...''\033[m')
    sleep(3)  # atrasa a resposta do comando em 3 segundos
    if pc == player:
        print('\033[1:32m''PARABÉNS! Você conseguiu me vencêr!')
    else:
        print('\033[1:31m''GANHEI! Eu pensei no número {} e não no {}!'.format(pc, player))
else:
    print('\033[1:31m''ERRO!''\033[m')
    print('\033[1:35m''Por que você digitou {}!? Eu falei um número de 0 a 5!'.format(player))
