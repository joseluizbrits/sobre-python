# Matriz em Python
'''Crie um programa que crie uma MATRIZ de
DIMENSÃO 3x3 e preencha com valores lidos
pelo teclado. No final mostre a MATRIZ na
tela, com a formatação correta'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('\033[1:37m''-=''\033[m' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()  # um print vazio para quebrar a linha
