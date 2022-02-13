# Jogo do Par ou Ímpar
'''Faça um programa que jogue PAR OU ÍMPAR com
o computador. O jogo só será interrompido quando
o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo'''

from random import randint
print('=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 10)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 20)
    pc = randint(0, 10)
    resultado = (valor + pc) % 2
    if resultado == 0:
        print(f'Você jogou {valor} e o computador jogou {pc}. Total de {valor+pc} DEU PAR')
        print('-' * 20)
        if jogador == 'P':
            print('\033[1:32m''Você VENCEU!''\033[m''\n''Vamos jogar novamete...')
            print('=-' * 10)
        else:
            print('\033[1:31m''Você PERDEU''\033[m')
            break
    else:
        print(f'Você jogou {valor} e o computador jogou {pc}. Total de {valor+pc} DEU ÍMPAR')
        if jogador == 'P':
            print('\033[1:31m''Você PERDEU!''\033[m')
            break
        else:
            print('\033[1:32m''Você VENCEU!''\033[m''\n''Vamos jogar novamente...')
            print('=-' * 10)
    cont += 1
print(f'GAME OVER! Você venceu {cont} vezes.')
