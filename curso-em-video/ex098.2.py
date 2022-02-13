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


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print('\033[1m'f'Contagem de {i} até {f} de {p} em {p}''\033[m')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f :
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('\033[1m''Agora é sua vez de personalizar a contagem!''\033[1m')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
