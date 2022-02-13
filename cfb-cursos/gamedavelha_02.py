# Jogo da Velha

from random import randrange
from colorama import Fore

jogarnovamente = 's'
jogadas = 0
quemJoga = 2  # 1 = CPU  -  2 = Jogador
maxJogadas = 9
vit = 'n'
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def tela():
    global velha
    global jogadas
    print('    0   1   2')
    for i, k in enumerate(velha):
        print(f'{i}:  {velha[i][0]} | {velha[i][1]} | {velha[i][2]}')
        if i < 2:
            print('   -----------')
    print(f'Jogadas: {Fore.GREEN}{jogadas}{Fore.RESET}')


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input('Linha..: '))
            c = int(input('Coluna.: '))
            while velha[l][c] != ' ':
                l = int(input('Linha..: '))
                c = int(input('Coluna.: '))
            velha[l][c] = 'X'
            jogadas += 1
            quemJoga = 1
        except:
            print(f'{Fore.RED}Jogada inválida{Fore.RESET}')


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = randrange(0, 3)
        c = randrange(0, 3)
        while velha[l][c] != ' ':
            l = randrange(0, 3)
            c = randrange(0, 3)
        velha[l][c] = 'O'
        jogadas += 1
        quemJoga = 2


def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'
        # Verificar Linhas
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria != 'n':
            break
        # Verificar Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != 'n':
            break
        # Verificar Diagonal 1
        soma = 0
        id = 0
        while id < 3:
            if velha[id][id] == s:
                soma += 1
            id += 1
        if soma == 3:
            vitoria = s
            break
        # Verificar Diagonal 2
        soma = 0
        idl = 0
        idc = 2
        while idc >= 0:
            if velha[idl][idc] == s:
                soma += 1
            idl += 1
            idc -= 1
        if soma == 3:
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2  # 1 = CPU  -  2 = Jogador
    maxJogadas = 9
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


while jogarnovamente != 'n':
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        tela()
        vit = verificarVitoria()
        if vit != 'n' or jogadas >= maxJogadas:
            break
    print(f'{Fore.RED}FIM DE JOGO{Fore.YELLOW}')
    if vit == 'X' or vit == 'O':
        print(f'Resultado: Jogador {vit} venceu')
    else:
        print('Resultado: Empate')
    jogarnovamente = input(f'{Fore.BLUE}Jogar novamente? [s/n]: {Fore.RESET}').lower()[0]
    redefinir()
