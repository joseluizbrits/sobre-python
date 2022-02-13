# Conversor de Medidas
'''Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros'''

n = float(input('Digite um número: '))
ncent = n * 100
nmili = n * 1000
# o termo :.2f é para formatar o número em duas casas decimais
print('Você digitou o número \033[7;1;40m{}\033[m o que corresponde a \033[1m{:.2f}\033[m metros'.format(n, n))
print('Isto equivale a \033[1m{:.2f}\033[m centímetros e a \033[1m{:.2f}\033[m milímetros'.format(ncent, nmili))
