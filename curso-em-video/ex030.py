# Par ou Ímpar?
'''Crie um programa que leia um número
inteiro e mostre na tela se ela é PAR ou ÍMPAR'''

numero = int(input('\033[1;35m''Me diga um número qualquer: '))
resultado = numero % 2 # Informará o resto da divisão por 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
