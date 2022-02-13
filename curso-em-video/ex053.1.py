# Detector de Palíndromo
'''Crie um programa que leia uma FRASE qualquer e
diga se ela é um PALÍNDROMO, desconsiderando os espaços
Ex: APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA'''

frase = str(input('Digite uma frase: ')).strip().upper()
divida = frase.split() # divisão da string
junta = ''.join(divida) # junção da string
inversa = ''
for letra in range(len(junta) - 1, -1, -1): # inversão das letras
    inversa += junta[letra]
print('O inverso de \033[1m''{} é {}''\033[m'.format(junta, inversa))
if inversa == junta:
    print('\033[32m''Que legal! A frase digitada é um palíndromo!')
else:
    print('\033[31m''A frase digitada não é um palíndromo!')
