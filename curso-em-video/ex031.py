# Custo da Viagem
'''Desenvolva um programa que pergunte a distância
de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até
200 km e R$ 0,45 para viagens mais longas'''

dist = float(input('\033[32m''Informe quantos km terá a sua viagem: '))
print('\033[30;43m''Você está prestes a iniciar uma viagem de {} km''\033[m'.format(dist))
if dist <= 200:
    pay = dist * 0.50
else:
    pay = dist * 0.45
print('\033[36m''O valor da sua passagem é de \033[1mR$ {:.2f}'.format(pay))
