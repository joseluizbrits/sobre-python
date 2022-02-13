# Aprimorando os Dicionários
'''Aprimore o ex093 para que ele funcione
com VÁRIOS JOGADORES, incluindo um sistema
de visualização de DETALHES DO APROVEITAMENTO
de cada jogador'''

estatistica = list()
jogador = dict()
gols = list()
while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    estatistica.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31m''ERRO! Responda apenas S ou N!''\033[m')
    if resp in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(estatistica):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogado (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(estatistica):
        print(f'\033[31mERRO! Não existe jogador com código {busca}!\033[m')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {estatistica[busca]["nome"]}:')
        for i, g in enumerate(estatistica[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
