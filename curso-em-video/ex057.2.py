# Validação de Dados
'''Faça um programa que leia o SEXO de uma pessoa, mas
só aceite os valores de 'M' e 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto'''

sexo = str(input('\033[1m''Informe seu sexo [M/F]: \033[m')).strip().upper()[0] # [0] para pegar só a primeira letra
while sexo not in 'MF': # enquanto não tiver a letra M ou a letra F na string
    sexo = str(input('\033[31m''Dados inválidos.''\033[m \033[1m''Por favor, informe seu sexo: \033[m')).strip().upper()[0]
print('Sexo \033[32m''{}''\033[m registrado com sucesso'.format(sexo))
