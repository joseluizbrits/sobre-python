# Dicionário em Python
'''Faça um programa que leia NOME e
MÉDIA de um aluno, guardando também
a SITUAÇÃO em um DICIONÁRIO. No final,
mostre o conteúdo da estrutura na tela'''

nome = str(input('Nome: '))
dicionario = dict()
while True:
    media = float(input(f'Média de {nome}: '))
    if 0 <= media <= 10:
        break
if media >= 6:
    dicionario['Situação'] = '\033[1:32m''Aprovado''\033[m'
else:
    dicionario['Situação'] = '\033[1:31m''Reprovado''\033[m'
print(f'Nome é igual a {nome}')
print(f'Média é igual a {media}')
print(f'Situação é igual a {dicionario["Situação"]}')
