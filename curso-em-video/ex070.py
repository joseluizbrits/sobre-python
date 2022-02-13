# Estatísticas em produtos
'''Crie um programa que leia o NOME e o PREÇO de
VÁRIOS PRODUTOS. O programa deverá perguntar se o
USUÁRIO vai continuar. No final, mostre:
A) Qual é o TOTAL GASTO na compra
B) Quantos produtos custam MAIS de R$ 1.000,00
C) Qual é o NOME do produto mais BARATO'''

cor = {'preta': '\033[1:30m', 'vermelho': '\033[31m', 'verde': '\033[32m',
       'amarelo': '\033[33m', 'azul': '\033[34m', 'roxona': '\033[1:35m',
       'negrito': '\033[1m', 'cinza': '\033[37m', 'limpar': '\033[m'}

print('{}-{}'.format(cor['preta'], cor['limpar']) * 35)
print('{}{: ^35}{}'.format(cor['roxona'], 'LOJAS BRITS', cor['limpar']))
print('{}-{}'.format(cor['preta'], cor['limpar']) * 35)
resposta = produtobarato = ' '
totalgasto = produtoscaros = menorpreco = contproduto = 0
while True:
    produto = str(input('{}Nome do Produto: '.format(cor['negrito'])))
    preco = float(input('{}Preço: R$ '.format(cor['negrito'])))
    totalgasto += preco
    contproduto += 1
    if preco > 1000:
        produtoscaros += 1
    if contproduto == 1 or preco < menorpreco:
            menorpreco = preco
            produtobarato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('{}Quer continuar? [S/N] '.format(cor['negrito']))).strip().upper()[0]
    if resposta == 'N':
        break
print('{}{:-^40}{}'.format(cor['roxona'], ' FIM DO PROGRAMA ', cor['limpar']))
print('{}O total da compra foi {}R$ {:.2f}{}'.format(cor['negrito'], cor['verde'], totalgasto, cor['limpar']))
print('\033[1m''Temos {}{}{}\033[1m produtos custando mais de {}R$ 1000.00{}'.format(cor['roxona'], produtoscaros, cor['limpar'], cor['vermelho'], cor['limpar']))
print('\033[1m''O produto mais barato foi {}{}{}\033[1m que custa {}R$ {:.2f}'.format(cor['roxona'], produtobarato, cor['limpar'], cor['azul'], menorpreco))
