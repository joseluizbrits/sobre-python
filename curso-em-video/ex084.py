# Lista composta e análise de dados
'''Faça um programa que leia NOME E PESO de VÁRIAS
PESSOAS, guardando tudo em uma LISTA. No final, mostre:
A) QUANTAS pessoas foram cadastradas
B) Uma listagem com as pessoas mais PESADAS
C) Uma listagem com as pessoas mais LEVES'''

pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('\033[1:35m''-=''\033[m' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
