# Tuplas com Times de Futebol
'''Crie uma TUPLA preenchida com os 20 PRIMEIROS
colocados da Tabela do CAMPEONATO BRASILEIRO DE
FUTEBOL,na ordem de colocação. Depois mostre:
A) Apenas os 5 PRIMEIROS colocados
B) Os ÚLTIMOS 4 colocados da tabela
C) Uma lista com os times em ORDEM ALFABÉTICA
D) Em que POSIÇÃO na tabela está o time da CHAPECOENSE'''

tabela = ('Flamengo', 'Internacional', 'Atlético-MG',
          'São Paulo', 'Fluminense', 'Grêmio',
          'Palmeiras', 'Santos', 'Athletico-PR',
          'Bragantino', 'Ceará SC', 'Corinthians',
          'Atlético-GO', 'Bahia', 'Sport Recife',
          'Fortaleza', 'Vasco da Gama', 'Goiás',
          'Coritiba', 'Botafogo')
print('\033[1:32m=\033[m' * 30)
print('\033[1:33m''{:^30}''\033[m'.format('BRASILEIRÃO 2020'))
print('\033[1:32m=\033[m' * 30)
posicao = 1
for clube in tabela:
    print('\033[1m''{}º {}''\033[m'.format(posicao, clube))
    posicao += 1
print('\033[1:32m''-=''\033[m' * 30)
print('\033[1m''Os 5 primeiros colocados:\033[32m {}''\033[m'.format(tabela[0:5]))
print('\033[1:32m''-=''\033[m' * 30)
print('\033[1m''Os 4 últimos colocados:\033[31m {}''\033[m'.format(tabela[-4:]))
print('\033[1:32m''-=''\033[m' * 30)
print('\033[1m''Os times em ordem alfabética:\033[m '.format(sorted(tabela)))
print('\033[1:32m''-=''\033[m' * 30)
print(f'\033[1m'f'O Bragantino ficou na {tabela.index("Bragantino")+1}ª posição')
print('\033[1:32m''-=''\033[m' * 30)
