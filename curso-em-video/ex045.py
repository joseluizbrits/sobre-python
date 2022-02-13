# GAME: Pedra Papel e Tesoura
'''Crie um programa que faça o computador jogar JOKENPÔ com você'''

from random import randint
from time import sleep
print('\033[1:7m''{: ^30}''\033[m'.format('VAMOS JOGAR!')) # o termo : ^30 é para centralizar a frase
print('''Tente me vencer! Escolha:
\033[1:35m[ 1 ]\033[m \033[1:37m''Pedra
\033[1:35m[ 2 ]\033[m \033[1:37m''Papel
\033[1:35m[ 3 ]\033[m \033[1:37m''Tesoura\033[m''')
player = int(input('\033[1m''Sua opção: '))
if 1 <= player <= 3:
    pc = randint(1, 3)
    print('\033[1:30m''{}'.format('JO...'), end=' ')
    sleep(1)
    print('{}'.format('KEN...'), end=' ')
    sleep(1)
    print('PÔ!''\033[m')
    print('\033[1m''=''\033[m' * 27)
    if pc == 1 and player == 1:
        print('\033[1:7m''{: ^}''\033[m'.format('EU: Pedra x Pedra :VOCÊ'))
        print('\033[1m''=''\033[m' * 27)
        print('\033[1:34m''É... Parece que deu EMPATE. Vamos de novo!')
    elif pc == 2 and player == 2:
        print('\033[1:7m''{: ^}''\033[m'.format('EU: Papel x Papel :VOCÊ'))
        print('\033[1m''=''\033[m' * 27)
        print('\033[1:34m''É... Parece que deu EMPATE. Vamos de novo!')
    elif pc == 3 and player == 3:
        print('\033[1:7m''{: ^}''\033[m'.format('EU: Tesoura x Tesoura :VOCÊ'))
        print('\033[1m''=''\033[m' * 27)
        print('\033[1:34m''É... Parece que deu EMPATE. Vamos de novo!')
    elif pc == 1:
        if player == 2:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Pedra x Papel :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:32m''Ah... Parabens! Desta vez você me VENCEU')
        elif player == 3:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Pedra x Tesoura :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:31m''VENCI! Hahaha... Talvez você tenha mais sorte na próxima')
    elif pc == 2:
        if player == 1:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Papel x Pedra :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:31m''VENCI! Hahaha... Talvez você tenha mais sorte na próxima')
        elif player == 3:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Papel x Tesoura :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:32m''Ah... Parabens! Desta vez você me VENCEU')
    elif pc == 3:
        if player == 1:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Tesoura x Pedra :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:32m''Ah... Parabens! Desta vez você me VENCEU')
        elif player == 2:
            print('\033[1:7m''{: ^}''\033[m'.format('EU: Tesoura x Papel :VOCÊ'))
            print('\033[1m''=''\033[m' * 27)
            print('\033[1:31m''VENCI! Hahaha... Talvez você tenha mais sorte na próxima')
else:
    print('\033[31m''Opção inválida. Tente novamente')
