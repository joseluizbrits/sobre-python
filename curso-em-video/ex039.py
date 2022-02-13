# Alistamento Militar
'''Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade,
se ele AINDA VAI SE ALISTAR ao serviço militar,
se é a HORA DE SE ALISTAR, ou seja, já PASSOU DO TEMPO
do alistamento. Seu programa também deverá mostrar o
tempo que falta ou que passou do prazo'''

from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano # date.today.year ano atual configurado na máquina
if idade == 19:
    print('\033[31m''Já passou do tempo de você se alistar!')
    print('Você deveria ter se alistado no ano passado!')
elif idade == 17:
    print('\033[33m''Fique atento! Você precisará se alistar no ano que vem!')
elif idade > 18:
    tempo = idade - 18
    print('\033[31m''Já passou do tempo de você se alistar!')
    print('Você está {} anos atrasado!'.format(tempo))
elif idade < 18:
    tempo = idade - 18
    print('\033[34m''Fique tranquilo! Ainda faltam {} anos para você se alistar!'.format(tempo))
else:
    print('\033[32m''Já está na hora de você se alistar, corra!')
