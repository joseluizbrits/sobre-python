# Maior e Menor valores
'''Crie um programa que leia VÁRIOS NÚMEROS
inteiros pelo telado. No final da execução,
mostre a MÉDIA ENTRE TODOS os valores e qual
foi o MAIOR e o MENOR valores lidos. O programa
deve perguntar ao usuário se ele quer ou não
CONTINUAR a digitar valores'''

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # [0] pra pergar só a 1ª letra
media = soma / quant
print('Você digitou \033[35m''{}''\033[m números e a média foi \033[35m''{:.2f}''\033[m'.format(quant, media))
print('O maior valor foi \033[35m''{}''\033[m e o menor foi \033[35m''{}'.format(maior, menor))
