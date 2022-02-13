# Soma ímpares múltiplos de três
'''Faça um programa que calcule a soma
entre todos os NÚMEROS ÍMPARES que são
MÚLTIPLOS DE TRÊS e que se encontram
no intervalo de 1 até 500'''

soma = 0 #acumulador
cont = 0 #contador
for n in range(1, 501, 2):
    if n % 3 == 0: # verificar se "n" é divisível por 3
        soma += n # soma += n é o mesmo que soma = soma + n
        cont += 1 # cont += 1 é o mesmo que cont = cont + 1
print('A soma de todos os \033[1:34m''{}''\033[m'' valores solicitados é \033[1:34m''{}'.format(cont, soma))
