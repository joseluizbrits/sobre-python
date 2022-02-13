# Média Aritmética
'''Desenvolva um programa que leia as duas
notas de um aluno, calcule e mostre a sua média'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('A média do aluno é \033[1m{}'.format(m))
if media >= 6:
    print('\033[1;32m''APROVADO''\033[m')
else:
    print('\033[1;31m''REPROVADO''\033[m')
