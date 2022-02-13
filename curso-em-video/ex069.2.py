# Análise de dados do grupo
'''Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO
quer ou não continuar. No final mostre:
 A) Quantas pessoas tem mais de 18 ANOS
 B) Quantos HOMENS foram cadastrados
 C) Quantas MULHERES tem menos de 20 ANOS'''

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: \033[35m'f'{tot18}''\033[m')
print('Ao todo temos \033[35m'f'{totH}''\033[m homens cadastrados')
print('E temos \033[35m'f'{totM20}''\033[m mulheres com menos de 20 anos')
