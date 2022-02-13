# Jogo da Velha

from random import randint

lista = [
    ['', '', ''],  # Linha 0
    ['', '', ''],  # Linha 1
    ['', '', '']   # Linha 2
]


def mostrar_jogo(s=None):
    print(f'\033[33m    0   1   2''\033[m')
    print(f'\033[34m{"0: "}\033[m', end='')
    for i, l in enumerate(lista[0]):
        if i == 2:
            print(f'{l.center(3)}', end='')
        else:
            print(f'{l.center(3)}', end='|')
    print(f'\n   {"-" * 11}')
    print(f'\033[34m{"1: "}\033[m', end='')
    for i, l in enumerate(lista[1]):
        if i == 2:
            print(f'{l.center(3)}', end='')
        else:
            print(f'{l.center(3)}', end='|')
    print(f'\n   {"-" * 11}')
    print(f'\033[34m{"2: "}\033[m', end='')
    for i, l in enumerate(lista[2]):
        if i == 2:
            print(f'{l.center(3)}', end='')
        else:
            print(f'{l.center(3)}', end='|')
    s = ''
    return s


def jogada_do_jogador():
    try:
        linha = int(input('\033[34m''Linha: \033[m'))
        coluna = int(input('\033[33m''Coluna: \033[m'))
    except:
        print('\033[31m''Digite uma posição válida''\033[m')
        jogada_do_jogador()
    else:
        try:
            if lista[linha][coluna] == '':
                lista[linha][coluna] = 'X'
            else:
                print('\033[31m''Campo já preenchido. Aposte em outro!''\033[m')
                jogada_do_jogador()
        except IndexError:
            print('\033[31m''Digite uma posição válida''\033[m')
            jogada_do_jogador()
        else:
            verificacao_de_vitoria_jogador()
            if verificacao_de_vitoria_jogador() is True:
                mostrar_jogo()
                return print('\n\033[1:32m''Você ganhou!''\033[m')


def verificacao_de_vitoria_jogador():
    if lista[0][0] == 'X' and lista[0][1] == 'X' and lista[0][2] == 'X':
        return True
    elif lista[1][0] == 'X' and lista[1][1] == 'X' and lista[1][2] == 'X':
        return True
    elif lista[2][0] == 'X' and lista[2][1] == 'X' and lista[2][2] == 'X':
        return True
    elif lista[0][0] == 'X' and lista[1][0] == 'X' and lista[2][0] == 'X':
        return True
    elif lista[0][1] == 'X' and lista[1][1] == 'X' and lista[2][2] == 'X':
        return True
    elif lista[0][2] == 'X' and lista[1][2] == 'X' and lista[2][2] == 'X':
        return True
    elif lista[0][0] == 'X' and lista[1][1] == 'X' and lista[2][2] == 'X':
        return True
    elif lista[0][2] == 'X' and lista[1][1] == 'X' and lista[2][0] == 'X':
        return True
    else:
        return False


def jogada_do_computador():
    linha = randint(0, 2)
    coluna = randint(0, 2)
    if lista[linha][coluna] == '':
        lista[linha][coluna] = 'O'
        verificacao_de_vitoria_computador()
        if verificacao_de_vitoria_computador() is True:
            mostrar_jogo()
            return print('\n\033[1:31m''Computador ganhou!''\033[m')
    else:
        jogada_do_computador()


def verificacao_de_vitoria_computador():
    if lista[0][0] == 'O' and lista[0][1] == 'O' and lista[0][2] == 'O':
        return True
    elif lista[1][0] == 'O' and lista[1][1] == 'O' and lista[1][2] == 'O':
        return True
    elif lista[2][0] == 'O' and lista[2][1] == 'O' and lista[2][2] == 'O':
        return True
    elif lista[0][0] == 'O' and lista[1][0] == 'O' and lista[2][0] == 'O':
        return True
    elif lista[0][1] == 'O' and lista[1][1] == 'O' and lista[2][2] == 'O':
        return True
    elif lista[0][2] == 'O' and lista[1][2] == 'O' and lista[2][2] == 'O':
        return True
    elif lista[0][0] == 'O' and lista[1][1] == 'O' and lista[2][2] == 'O':
        return True
    elif lista[0][2] == 'O' and lista[1][1] == 'O' and lista[2][0] == 'O':
        return True
    else:
        return False


resp = 'S'
jogadas = 0
while True:
    print(mostrar_jogo())
    jogada_do_jogador()
    if verificacao_de_vitoria_jogador() is True:
        break
    jogada_do_computador()
    if verificacao_de_vitoria_computador() is True:
        break
    jogadas += 1
    if jogadas == 4:
        print(mostrar_jogo())
        jogada_do_jogador()
        if verificacao_de_vitoria_jogador() is False and verificacao_de_vitoria_computador() is False:
            print('\033[1:33m''Deu Velha!')
        break
