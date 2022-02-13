# Radar eletrônico
'''Escreva um programa que leia a velocidade de
um carro. Se ela ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai
custar R$ 7,00 por cada km acima do limite'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[1;31m''MULTADO!''\033[m''Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Você terá de pagar uma multa de ''\033[1;31m''R$ {:.2f}''\033[m''!'.format(multa))
print('\033[32m''Tenha um bom dia! Dirija com segurança!')
