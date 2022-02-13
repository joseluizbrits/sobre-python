# Matriz em Python
'''Crie um programa que crie uma MATRIZ de
DIMENSÃO 3x3 e preencha com valores lidos
pelo teclado. No final mostre a MATRIZ na
tela, com a formatação correta'''

matriz = list()
for c in range(0, 3):
    v = int(input(f'Digite um valor para [0, {c}]: '))
    matriz.append(v)
for c in range(0, 3):
    v = int(input(f'Digite um valor para [1, {c}]: '))
    matriz.append(v)
for c in range(0, 3):
    v = int(input(f'Digite um valor para [2, {c}]: '))
    matriz.append(v)
print('\033[1:37m''-=''\033[m' * 30)
print(f'[   {matriz[0]}   ][   {matriz[1]}   ][   {matriz[2]}   ]')
print(f'[   {matriz[3]}   ][   {matriz[4]}   ][   {matriz[5]}   ]')
print(f'[   {matriz[6]}   ][   {matriz[7]}   ][   {matriz[8]}   ]')
