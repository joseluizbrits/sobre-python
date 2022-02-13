# Análise de dados do grupo
'''Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO
quer ou não continuar. No final mostre:
 A) Quantas pessoas tem mais de 18 ANOS
 B) Quantos HOMENS foram cadastrados
 C) Quantas MULHERES tem menos de 20 ANOS'''

resposta = ' '
maiorde18 = homens = mulheres = 0
while resposta != 'N':
    print('-' * 25)
    print('\033[35m''CADASTRE UMA PESSOA''\033[m')
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade > 18:
        maiorde18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while True:
        if sexo in 'M':
            homens += 1
            break
        elif sexo in 'F' and idade < 20:
            mulheres += 1
            break
        elif sexo in 'F':
            break
        else:
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while True:
        if resposta in 'SN':
            break
        else:
            resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('====== \033[35m''FIM DO PROGRAMA''\033[m ======')
print('Total de pessoas com mais de 18 anos: \033[35m'f'{maiorde18}''\033[m')
print('Ao todo temos \033[35m'f'{homens}''\033[m homens cadastrados')
print('E temos \033[35m'f'{mulheres}''\033[m mulheres com menos de 20 anos')
