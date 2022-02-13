# Analisando Triângulo v1.0
'''Desenvolva um programa que leia o
comprimento de três resta e diga ao usuário
se elas podem ou não formar um triângulo.'''

print('\033[1:35m''-=' * 13)
print('Analisador de Triângulos')
print('-=' * 13)
r1 = float(input('\033[m''Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1:32m''Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('\033[1:31m''Os segmentos acima NÃO PODEM FORMAR um triângulo!')
