# Índice de Massa Corporal
'''Desenvolva uma lógica que leia o peso e a
altura de uma pessoa, calcule seu IMC e mostre
seu status, de acordo com a tabela abaixo:
- Abaixo de 18,5: ABAIXO DO PESO
- Entre 18,5 e 25: PESO IDEAL
- 25 até 30: SOBREPESO
- 30 até 40: OBESIDADE
- Acima de 40: OBESIDADE MÓRBIDA'''

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (m): '))
if 20 < peso < 300 and 1 < altura < 2.5:
    imc = peso / altura ** 2
    print('IMC: {:.2f}'.format(imc))
    if imc <= 18.5:
        print('SITUAÇÃO: \033[1:33m''Abaixo do peso')
    elif imc <= 25:
        print('SITUAÇÃO: \033[1:32m''Peso ideal')
    elif imc <= 30:
        print('SITUAÇÃO: \033[1:34m''Sobrepeso')
    elif imc <= 40:
        print('SITUAÇÃO: \033[1:33m''Obesidade')
    else:
        print('SITUAÇÃO: \033[1:31m''Obesidade mórbida')
else:
    print('\033[31m''Valores inválidos. Tente novamente')
