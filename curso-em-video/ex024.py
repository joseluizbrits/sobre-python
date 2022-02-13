# Verificando as primeiras letras de um texto
'''Crie um programa que leia o nome de uma
cidade e diga se ela começa ou não com o nome "SANTO"'''

cid = str(input('\033[1;37m''Digite o nome de sua cidade:\033[m ')).strip()
print(cid[:5].upper() == 'SANTO')
