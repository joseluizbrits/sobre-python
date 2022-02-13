# Conversor de Bases Numéricas
'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
- 1 para BINÁRIO
- 2 para OCTAL
- 3 para HEXADECIMAL'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
option = int(input('Sua opção: '))
if option == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) # [2:] fatiamento da string
elif option == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[1:31m''Opção invalida. Tente novamente')
