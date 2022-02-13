# Primeiro e último nome de uma pessoa
'''Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente
Ex: nome: José Luiz Brits; primeiro: José; último; Brits'''

n = str(input('\033[1;37m''Digite o seu nome completo:\033[m ')).strip()
nome = n.split()
print('\033[35m''Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))

# strip() serve para remover o espaços ínuteis antes e depois da string
# split() serve para dividir as palavras da string
