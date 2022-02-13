# Progressão Aritmética
'''Desenvolva um programa que leia o PRIMEIRO
TERMO e a RAZÃO de uma PA. No final, mostre
os 10 primeiros termos dessa progressão'''

print('\033[1m''-=' * 10)
print('Gerador de PA')
print('-=' * 10)
n = int(input('\033[m''Primeiro termo: '))
r = int(input('Razão: '))
termo10 = n + (10 - 1) * r
for c in range(n, termo10 + r, r): # range(primeiro termo, décimo termo, razão)
    print('{}'.format(c), end=' ➔ ')
print('\033[1:37m''FIM')
