# Radar eletrônico
'''Escreva um programa que leia a velocidade de
um carro. Se ela ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai
custar R$ 7,00 por cada km acima do limite'''

vcar = int(input('\033[1m''Informe em quantos km/h está a velocidade do carro: '))
vmax = 80
if vcar < vmax:
    print('\033[1;32m''Ok, está tudo bem. Pode seguir em frente e tenha uma boa viagem!')
else:
    vdif = vcar - vmax
    pay = 7 * vdif
    print('\033[1;33m''O limite de velocidade é {} km/h'.format(vmax))
    print('O seu carro está {} km/h acima do permitido!'.format(vdif))
    print('\033[1;31m''Infelizmente terá de ser aplicada uma multa de R$ {:.2f} pela infração'.format(pay))
