# Contagem regressiva
'''Faça um programa que mostre na tela uma
CONTAGEM REGRESSIVA para o estouro de fogos
de artifício, indo de 10 até 0, com uma
pausa de 1 SEGUNDO entre eles'''

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1:33:41m''BOOM! BOOM! BOOM!''\033[m')
