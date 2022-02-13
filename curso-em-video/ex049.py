# Tabuada v.2.0
'''Refaça o DESAFIO 009, mostrando a
TABUADA de um número que o usuário escolher,
só que agora utilizando um LAÇO FOR'''

n = int(input('Digite um número: '))
print('A tabuada do número \033[32m''{}''\033[m é:'.format(n))
for c in range(1, 11):
    print('{} x {} = \033[34m''{}''\033[m '.format(n, c, n*c))
