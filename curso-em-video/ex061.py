# Progressão Aritmética v2.0
'''Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e
a RAZÃO de uma PA, mostrando o 10 PRIMEIROS TERMOS
da progressão usando a estrutura WHILE'''

print('\033[1m''-=' * 10)
print('Gerador de PA')
print('-=' * 10)
n = int(input('\033[m''Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{} ➔ '.format(termo), end='')
    termo += r
    cont += 1
print('\033[1:37m''FIM')
