# Validação de Dados
'''Faça um programa que leia o SEXO de uma pessoa, mas
só aceite os valores de 'M' e 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1m''Qual é o seu sexo? [M/F]: \033[m')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('\033[31m''ERRO! Por favor, digite M para masculino ou F para feminino.\033[m')
if sexo == 'M':
    print('\033[1:32m''Você é um homem!')
else:
    print('\033[1:32m''Você é uma mulher!')
