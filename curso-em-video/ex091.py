# Jogo de Dados em Python
'''Crie um programa onde 4 JOGADORES joguem
um DADO e tenham resultados ALEATÓRIOS. Guarde
esses resultados em um DICIONÁRIO. No final,
coloque esse dicionário em ordem, sabendo que
o VENCEDOR tirou o MAIOR NÚMERO no dado'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('\033[1m''Valores sorteados:''\033[m')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\033[1m''-=' * 30)
print('  == RANKING DOS JOGADORES ==''\033[m')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
