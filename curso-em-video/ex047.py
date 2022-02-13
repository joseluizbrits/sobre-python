# Contagem de pares
'''Crie um programa que mostre na tela TODOS OS
NÚMEROS PARES que estão no interválo entre 1 e 50'''

for n in range(2, 51, 2):
    print(n, end=' ')
print('\033[1:37m''FIM')

# range(2, 51, 2) significa um intervalo de 2 a 50, pulando de 2 em 2
# lembre-se que o Python despreza o último número, por isso que é (2, 51)
