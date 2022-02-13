# Sistema interativo de ajuda em Python
'''Faça um MINI-SISTEMA que utilize o Interactive
Help do Python. O usuário vai digitar o COMANDO e
o MANUAL vai aparecer. Quando o usuário digitar a
palavra 'FIM', o programa se ENCERRARÁ
OBS: Use CORES'''

from time import sleep

c = ('\033[m',      # 0 - sem cores
     '\033[41m',    # 1 - vermelho
     '\033[42m',    # 2 - verde
     '\033[43m',    # 3 - amarelo
     '\033[44m',    # 4 - azul
     '\033[45m',    # 5 - roxo
     '\033[7;40m',  # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
