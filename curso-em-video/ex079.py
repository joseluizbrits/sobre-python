# Valores únicos em uma Lista
'''Crie um programa onde o usuário possa digitar vários
VALORES NUMÉRICOS e cadastre-os em uma LISTA. Caso número
já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final,
serão exibidos todos os VALORES ÚNICOS digitados, em
ORDEM CRESCENTE'''

valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('\033[32m''Valor adicionado com sucesso...\033[m')
    else:
        print('\033[31m''Valor duplicado! não vou adicionar...\033[m')
    r = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('\033[1:34m''=-''\033[m' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
