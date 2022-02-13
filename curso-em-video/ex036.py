# Aprovando Empréstimo
'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o VALOR DA CASA, o SALÁRIO do
comprador e em QUANTOS anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado'''

casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
ano = int(input('Informe em quantos anos pretende quitar a casa: '))
prestacao = casa / (ano * 12)
if prestacao > (salario * 0.3):
    print('\033[1;31m''EMPRÉSTIMO NEGADO''\033[m')
    print('Infelizmente você não terá condições de quitar esta casa')
else:
    print('\033[1;32m''EMPRÉSTIMO APROVADO''\033[m')
    print('O valor das parecelas serão de \033[1m''R$ {:.2f}'.format(prestacao))
