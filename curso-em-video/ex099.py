# Função que descobre o maior
'''Faça um programa que tenha uma FUNÇÃO
chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o MAIOR'''

from time import sleep

def maior(* num):
    print('\033[1m''-=' * 30)
    print('Analisando os valores passados...''\033[m')
    maior = 0
    for i, n in enumerate(num):
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
        if i == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
