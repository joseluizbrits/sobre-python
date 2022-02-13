# Conversor de moedas
'''Crie um programa que leia quanto
dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar
* Considere US$ 1,00 = R$ 3,27'''

n = float(input('\033[1;34m''Informe quantos reais você têm na carteira: \033[m'))
x: float = n // 3.27
print('\033[1;32m''Com R$ {:.2f} você pode comprar U$ {:.2f}.'.format(n, x))
