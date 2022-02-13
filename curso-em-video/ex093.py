# Cadastro de Jogador de Futebol
'''Crie um programa que gerencie o aproveitamento de
um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO
JOGADOR e QUANTAS PARTIDAS ele jogou. Depois vai ler
a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final,
tudo isso será guardado em um dicionário, incluindo o
TOTAL DE GOLS feitos durante o campeonato'''

estatistica = dict()
gols = list()
estatistica['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {estatistica["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
estatistica['gols'] = gols[:]
estatistica['total'] = sum(gols)
print('\033[1:37m''-=''\033[m' * 30)
print(estatistica)
print('\033[1:37m''-=''\033[m' * 30)
for k, v in estatistica.items():
    print(f'O campo {k} tem o valor {v}')
print('\033[1:37m''-=''\033[m' * 30)
print(f'O jogador {estatistica["nome"]} jogou {partidas} partidas')
for p, g in enumerate(estatistica['gols']):
    print(f'    => Na partida {p+1}, fez {g} gols')
print(f'Foi um total de {estatistica["total"]} gols')
