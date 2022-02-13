# Vários números com flag
'''Crie um programa que leia VÁRIOS NÚMEROS
inteiros pelo teclado. O programa só vai parar
quando o usuário digitar 999, que é a CONDIÇÃO
DE PARADA. No final, mostre QUANTOS NÚMEROS foram
digitados e qual foi a SOMA entre eles'''
# DESCONSIDERANDO O FLAG, ou seja, o número 999

n = c = s = 0
while True: # um loop infinito, ou seja, um enquanto (while) infinito
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break # comando para sair do while infinito
    c += 1
    s += n
print(f'A soma dos \033[35m'f'{c}''\033[m valores foi \033[35m'f'{s}''\033[m!')
# O "f" no início do print representa o fstring, uma maneira de simplificar o .format()
