# Função de Contador
'''Faça um programa que tenha uma FUNÇÃO
chamada contador(), que receba três PARÂMETROS:
INÍCIO, FIM e PASSO e realize a contagem. Seu
programa tem que realizar TRÊS CONTAGENS através
da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem PERSONALIZADA'''

from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim and passo > 0:
        print('-=' * 20)
        print('\033[1m'f'Contagem de {inicio} até {fim} de {passo} em {passo}''\033[m')
        sleep(2.5)
        for c in range(inicio, fim - 1, - passo):
            print(c, end=' ', flush=True)   # o flush=True é para não ligar o "buffer de tela"
            sleep(0.5)                      # e poder mostrar o sleep(0.5)
        print('FIM!')
    if fim > inicio:
        print('-=' * 20)
        print('\033[1m'f'Contagem de {inicio} até {fim} de {passo} em {passo}''\033[m')
        sleep(2.5)
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    if passo < 0:
        print('-=' * 20)
        print('\033[1m'f'Contagem de {inicio} até {fim} de {- passo} em {- passo}''\033[m')
        sleep(2.5)
        for c in range(inicio, fim - 1, passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    if passo == 0:
        if inicio > fim:
            print('-=' * 20)
            print('\033[1m'f'Contagem de {inicio} até {fim} de 1 em 1''\033[m')
            sleep(2.5)
            for c in range(inicio, fim - 1, - 1):
                print(c, end=' ', flush=True)
                sleep(0.5)
            print('FIM!')
        if inicio < fim:
            print('-=' * 20)
            print('\033[1m'f'Contagem de {inicio} até {fim} de 1 em 1''\033[m')
            sleep(2.5)
            for c in range(inicio, fim + 1):
                print(c, end=' ', flush=True)
                sleep(0.5)
            print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('\033[1m''Agora é sua vez de personalizar a contagem!''\033[m')
inicio = int(input('\033[1m''Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  \033[m'))
contador(inicio, fim, passo)
