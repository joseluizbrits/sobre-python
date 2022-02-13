# Classificando Atletas
'''A Confederação Nacional de Natação precisa
de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com sua idade:
- Até 9 anos: MIRIRM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date
anoatleta = int(input('Ano de nascimento do atleta: '))
anoatual = date.today().year
if (anoatual - 50) < anoatleta < anoatual:
    idade = anoatual - anoatleta
    if idade == 1:
        print('O atleta possui {} ano'.format(idade))
    else:
        print('O atleta possui {} anos'.format(idade))
    if idade <= 9:
        print('Categoria: \033[32m''MIRIM''\033[m')
    elif idade <= 14:
        print('Categoria: \033[34m''INFANTIL''\033[m')
    elif idade <= 19:
        print('Categoria: \033{33m''JÚNIOR''\033[m')
    elif idade <= 25:
        print('Categoria: \033[35m''SÊNIOR''\033[m')
    else:
        print('Categoria: \033[31m''MASTER''\033[m')
else:
    print('\033[31m''Valor inválido. Tente novamente')
