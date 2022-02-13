# Aluguel de Carros
'''Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado'''

day = int(input('\033[1;37m''Digite a quantidade de dias que o carro ficou alugado: '))
km = float(input('Digite a quantidade de km rodados: '))
pay = (day * 60) + (km * 0.15)
print('\033[1;30;43m''O total a pagar é de R${:.2f}\033[m'.format(pay))
