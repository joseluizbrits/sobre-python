# Sorteando uma ordem na lista
'''O mesmo professor do desafio anterior
quer sortear a ordem de apresentação de
trabalhos do alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada'''

from random import shuffle
n1 = str(input('\033[37m''Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
n5 = str(input('Quinto nome: \033[m'))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print(lista)
