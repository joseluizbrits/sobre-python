# Dobro, Triplo, Raiz Quadrada
'''Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada'''

n = float(input('Digite um número: '))
n2 = n * 2
n3 = n * 3
nx = n ** (1/2)
# o termo :.2f é para formatar o número em duas casa decimais
print('O número que você escolheu é o \033[7:40m{:.2f}\033[m'.format(n))
print('O dobro dele é \033[7:40m{:.2f}\033[m e o triplo é \033[7:40m{:.2f}\033[m'.format(n2, n3))
print('Já a sua raíz quadrada é \033[7:40m{:.2f}\033[m'.format(nx))
