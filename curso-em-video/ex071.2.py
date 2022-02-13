# Simulador de Caixa Eletrônico
'''Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No início, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro)
e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
OBS: Considere que o caixa possue cédulas de R$ 50, R$ 20, R$ 10 e R$ 1'''

print('\033[1:7:30:47m=\033[m' * 30)
print('\033[1:35:40m{:^30}\033[m'.format('CAIXA ELETRÔNICO'))
print('\033[1:7:30:47m=\033[m' * 30)
valor = int(input('\033[1m''Que valor você quer sacar? R$\033[m '))
total = valor
cedula = 50
totcedula = 0
while True:
    # ELIMINANDO AS NOTAS
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R$ {cedula}')
        # TROCANDO DE NOTA
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
