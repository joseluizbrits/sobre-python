# Conversor de Temperaturas
'''Escreva um programa que converta uma
temperatura digitada em °C e converta para °F'''

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de \033[7;40m''{}°C\033[m corresponde a \033[7;40m''{}°F''\033[m!'.format(c, f))
