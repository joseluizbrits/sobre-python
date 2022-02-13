# Ano Bissexto
'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

from datetime import date
print('\033[1m''Qual ano você deseja analisar?')
ano = int(input('\033[37m''Para analisar o ano atual, digite 0: \033[m'))
if ano == 0:
    ano = date.today().year     # Pegará o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;32m''é BISSEXTO'.format(ano))
else:
    print('O ano {} \033[1;31m''NÃO é BISSEXTO'.format(ano))
