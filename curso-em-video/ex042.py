# Analisando Triângulos v2.0
'''Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lado iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes'''

print('\033[7:1:37:40m''-=' * 15, end='')
print('-=''\033[m')
print('\033[7:1:37:40m    Analisador de Triângulos    \033[m')
print('\033[7:1:37:40m''-=' * 15, end='')
print('-=''\033[m')
r1 = float(input('\033[1m''Primeiro segmento: '))
r2 = float(input('\033[1m''Segundo segmento: '))
r3 = float(input('\033[1m''Terceiro segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1:32m''PODEM FORMAR''\033[m um triângulo', end=' ')
    if r1 == r2 == r3:
        print('\033[1m''EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('\033[1m''ESCALENO')
    else:
        print('\033[1m''ISÓSCELES')
else:
    print('Os segmentos acima \033[1:31m''NÃO PODEM FORMAR''\033[m um triângulo')
