# Grupo da Maioridade
'''Crie um programa que leia o ANO DE NASCIMENTO de
SETE PESSOAS. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores'''

from datetime import date
anoatual = date.today().year # Pegará o ano atual configurado na máquina
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    if 1900 < anonasc < anoatual:
        idade = anoatual - anonasc
        if idade >= 21:
            totalmaior += 1
        else:
            totalmenor += 1
    else:
        print('\033[31m''Ocorreu um erro no ano em que você digitou! Tente novamente.')
print('Há {} pessoas neste grupo que estão na maioridade'.format(totalmaior))
print('E há {} pessoas que ainda são menor de idade'.format(totalmenor))
