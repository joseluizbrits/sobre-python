# Unindo dicionários e listas
'''Crie um program que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS,
guardando os dados de cada pessoa em um DICIONÁRIO e todos os dicionários
em uma LISTA. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A MÉDIA de idade do grupo
C) Uma lista com todas as MULHERES
D) Uma lista com todas as pessoas com IDADE acima da MÉDIA'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\033[31m''ERRO! Por favor, digite apenas M ou F''\033[m')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31m''ERRO! Responda apenas S ou N''\033[m')
    if resp == 'N':
        break
print('\033[1:37m''-=''\033[m' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoa que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
