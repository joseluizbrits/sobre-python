# Jogo do Par ou Ímpar
'''Faça um programa que jogue PAR OU ÍMPAR com
o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1:32m''Você VENCEU!''\033[m')
            v += 1
        else:
            print('\033[1:31m''Você PERDEU!''\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1:32m''Você VENCEU!''\033[m')
            v += 1
        else:
            print('\033[1:31m''Você PERDEU!''\033[m')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
