# Extraindo dados de uma Lista
'''Crie um programa que vai ler VÁRIOS NÚMEROS
e colocar em uma LISTA. Depois disso, mostre:
A) QUANTOS números foram digitados
B) A lista de valores, ordenada de forma DECRESCENTE
C) Se o valor 5 foi digitado e está ou não na LISTA'''

lista = []
resp = 'S'
while resp in 'Ss':
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? \033[1:37m''[S/N] \033[m')).upper().strip()[0]
print('\033[1:35m''-=''\033[m' * 30)
print(f'\033[1mVocê digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
