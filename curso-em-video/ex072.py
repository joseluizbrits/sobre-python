# Número por Extenso
'''Crie um programa que tenha uma TUPLA totalmente
preenchida com uma contagem por extenso, de ZERO
até VINTE. Seu programa deverá ler um número pelo
teclado (ENTRE 0 e 20) e mostrá-lo por EXTENSO'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
resp = 'S'
while resp in 'Ss':
    while True:
        n = int(input('Digite um número entre zero e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número \033[35m{contagem[n]}\033[m')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
