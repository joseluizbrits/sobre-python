# Jogo da Adivinhação v.1.0
'''Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
print('\033[40;31m''Vamos lá! Tente adivinhar o número que o computador está pensando...\033[m')
npc = randint(0, 5)
n = int(input('\033[1m''Escolha um número inteiro de 0 a 5: \033[m'))
if npc == n:
    print('\033[1;32m''Nossa, você acertou! Era justamente o número {}!'.format(n))
else:
    print('\033[1;31m''Que pena... Você colocou o número {} e o computador estava pensando no número {}'.format(n, npc))
