# Listas com pares e ímpares
'''Crie um programa onde o usuário possa digitar
SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA
ÚNICA que mantenha separados os valores PARES E ÍMPARES.
No final, mostre os valores pares e ímpares em ordem CRESCENTE'''

valores = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v}o. valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort() and valores[1].sort()
print('\033[1:37m''-=''\033[m' * 30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
