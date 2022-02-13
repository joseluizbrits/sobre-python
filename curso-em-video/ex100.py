# Funções para sortear e somar
'''Faça um programa que tenha uma LISTA
chamada NÚMEROS e duas FUNÇÕES chamadas
sorteia() e somaPar(). A primeira função
vai sortear 5 NÚMEROS e vai colocá-los dentro
da lista e a segunda função vai mostrar a SOMA
entre todos os valores PARES sorteados pela
função anterior'''

from time import sleep
from random import randint


def sorteia(lista):
    for n in range(0, 5):
        lista.append(randint(1, 10))
    print('\033[1m''Sorteando os valores da lista: ', end='')
    for n in lista:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
