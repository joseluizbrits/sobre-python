# Simulador de Caixa Eletrônico
'''Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No início, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro)
e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
OBS: Considere que o caixa possue cédulas de R$ 50, R$ 20, R$ 10 e R$ 1'''

print('\033[1:7:30:47m=\033[m' * 30)
print('\033[1:35:40m{:^30}\033[m'.format('CAIXA ELETRÔNICO'))
print('\033[1:7:30:47m=\033[m' * 30)

valor = int(input('\033[1m''Que valor você quer sacar? R$\033[m '))
notasde50 = valor // 50
print(f'Total de {notasde50} cédulas de R$ 50,00')
resto50 = valor % 50
notasde20 = resto50 // 20
print(f'Total de {notasde20} cédulas de R$ 20,00')
resto20 = resto50 % 20
notasde10 = resto20 // 10
print(f'Total de {notasde10} cédulas de R$ 10,00')
resto10 = resto20 % 10
notasde1 = resto10 // 1
print(f'Total de {notasde1} cédulas de R$ 1,00')
