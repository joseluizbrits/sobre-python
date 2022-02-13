# Maior e menor da sequência
'''Faça um programa que leia o PESO de
CINCO PESSOAS. No final mostre qual foi
o MAIOR e o MENOR pelo lidos'''

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('\033[1m''Digite o peso da {}ª pessoa: \033[m'.format(p)))
    if p == 1: # verificando a primeira pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))
