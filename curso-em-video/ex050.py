# Soma dos pares
'''Desenvolva um programa que leia
SEIS NÚMEROS INTEIROS e mostre a soma
daqueles que apenas forem PARES. Se o
valor digitado for ÍMPAR, desconsidere-o'''

soma = 0 #acumulador
cont = 0 #contador
for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0: # verificando se o número é par
        soma += n # soma dos números pares
        cont += 1 # contagem dos números pares
if cont == 0:
    print('Você só informou números \033[1:31m''ÍMPARES')
elif cont == 1:
    print('Você informou {} número \033[1:32m''PAR''\033[m que é o {}'.format(cont, soma))
else:
    print('Você informou {} números \033[1:32m''PARES''\033[m e soma deles é {}'.format(cont, soma))
