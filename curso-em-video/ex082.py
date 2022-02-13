# Dividindo valores em várias listas
'''Crie um programa que vai ler VÁRIOS NÚMEROS
e colocar em uma LISTA. Depois disso, crie DUAS
LISTAS EXTRAS que vão conter apenas os valores
PARES e os valores ÍMPARES digitados, respectivamente.
Ao final, mostre o conteúdo das TRÊS LISTAS geradas'''

numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? \033[1:37m''[S/N] \033[m'))
    if resp in 'Nn':
        break
print('\033[1:35m''-=''\033[m' * 30)
print(f'A lista completa é {numeros}')
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    if n % 2 == 1:
        impares.append(n)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
