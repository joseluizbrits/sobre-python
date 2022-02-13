# Reajuste Salarial
'''Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15% de aumento'''

x = float(input('\033[1;37m''Digite o seu salário: \033[m'))
x1 = x * 1.15
print('\033[37m''No próximo mês, seu salário de \033[1;37m''R$', end= ' ')
print('{:.2f}\033[m \033[37m''aumentará para \033[1;30;42m''R$ {:.2f}\033[m'.format(x, x1))
