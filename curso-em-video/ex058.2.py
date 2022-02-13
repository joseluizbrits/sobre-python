# Jogo da Adivinhação v2.0
'''Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora
o jogador vai tentar advinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''

from random import randint
computador = randint(0, 10)
print('\033[35m''Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?''\033[m')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[35m''Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[34m''Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('\033[33m''Menos... Tente mais uma vez.')
print('\033[1:32m''Acertou com {} tentativas. Parabéns!'.format(palpites))
