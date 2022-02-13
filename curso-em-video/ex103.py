# Ficha do Jogador
'''Faça um programa que tenha uma FUNÇÃO
chamada ficha(), que receba dois PARÂMETROS
OPCIONAIS: o NOME de um jogador e quantos GOLS
ele marcou. O programa deverá ser capaz de mostrar
a FICHA DO JOGADOR, mesmo que algum dado não tenha
sido informado corretamente'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato')


# Programa Pricipal
n = str(input('\033[1m''Nome do Jogador: ')).title()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
