# Unindo dicionários e listas
'''Crie um program que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS,
guardando os dados de cada pessoa em um DICIONÁRIO e todos os dicionários
em uma LISTA. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A MÉDIA de idade do grupo
C) Uma lista com todas as MULHERES
D) Uma lista com todas as pessoas com IDADE acima da MÉDIA'''

dados = list()
pessoa = dict()
mulheres = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            if pessoa['sexo'] == 'F':
                mulheres.append((pessoa['nome']))
            break
        print('\033[31m''ERRO! Por favor, digite apenas M ou F''\033[m')
    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31m''ERRO! Por favor, digite apena M ou F''\033[m')
    if resp == 'N':
        break
print('\033[1:37m''-=''\033[m' * 30)
print(f'- O grupo tem {len(dados)} pessoas')
soma = 0
for i, p in enumerate(dados):
    soma += dados[i]["idade"]
media = soma / len(dados)
print(f'- A média de idade é de {media:5.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m, end=' ')
print('\n- Lista das pessoas que estão acima da média:')
for i, p in enumerate(dados):
    if dados[i]["idade"] > media:
        print(f'nome = {dados[i]["nome"]}; sexo = {dados[i]["sexo"]}; idade = {dados[i]["idade"]}')
print('<< ENCERRADO >>')
