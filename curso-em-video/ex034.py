# Aumentos múltiplos
'''Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Informe o valor do seu salário atual: '))
print('O seu salário é de \033[1;30m''R${:.2f}\033[m'.format(salario))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Você receberá um aumento de \033[1;32m''R$ {:.2f}\033[m'.format(aumento))
novo = salario + aumento
print('A partir de agora, o seu salário será de \033[1;30;42m''R$ {:.2f}\033[m'.format(novo))
print('\033[1;32m''PARABENS!')
