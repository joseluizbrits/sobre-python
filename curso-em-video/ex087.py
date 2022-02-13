# Mais sobre Matriz em Python
'''Aprimore o DESAFIO ANTERIOR, mostrando no final:
A) A SOMA de todos os VALORES PARES digitados
B) A SOMA dos valores da TERCEIRA COLUNA
C) O MAIOR valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('\033[1:37m''-=''\033[m' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()  # um print vazio para quebrar a linha
print('\033[1:37m''-=''\033[m' * 30)
print(f'A soma dos valores pares é {somapares}')
for l in range(0, 3):
    somacoluna3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna3}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
