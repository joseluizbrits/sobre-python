# Jogo da Adivinhação v2.0
'''Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora
o jogador vai tentar advinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador "PENSAR", ou seja, gera um número aleatório de 0 a 5
print('\033[1:33m''-=-''\033[m' * 20)
print('\033[35m''Vou pensar em um número entre 0 e 5. Tente adinhar...''\033[m')
print('\033[1:33m''-=-''\033[m' * 20)
player = -1
tentativas = 1
while pc != player:
    player = int(input('\033[35m''Em que número eu pensei? '))  # Jogador tenta adivinhar
    if 0 <= player <= 5 and pc != player:
        print('\033[7:37m''PROCESSANDO...''\033[m')
        sleep(2)  # atrasa a resposta do comando em 2 segundos
        print(pc)
        print('\033[1:31m''GANHEI! Eu não pensei no número {}! HAHAHA''\033[m'.format(player))
        print('\033[35m''Vamos lá, tente novamente!''\033[m')
        player += 1
        tentativas += 1
    elif pc != player:
        print('\033[1:31m''ERRO!''\033[m')
        print('\033[35m''Por que você digitou {}!? Eu falei um número de 0 a 5!'.format(player))
        print('\033[35m''Vamos lá, tente de novo.', end=' ')
print('\033[7:37m''PROCESSANDO...''\033[m')
sleep(2)  # atrasa a resposta do comando em 3 segundos
print('\033[1:32m''PARABÉNS! Você conseguiu me vencêr!''\033[m')
print('\033[35m''Foram {} tentativas para você conseguir isso!'.format(tentativas))
