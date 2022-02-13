# Cadastro de Trabalhador em Python
'''Crie um programa que leia NOME, ANO DE NASCIMENTO
e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em um
DICIONÁRIO se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ANO DE CONTRATAÇÃO e
o SALÁRIO. Calcule e acrescente, além da IDADE, com
quantos anos a pessoa vai e APOSENTAR'''

from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
print(trabalhador)
print('\033[1:37m''-=''\033[m' * 30)
for k, v in trabalhador.items():
    print(f'  - {k} tem o valor {v}')
