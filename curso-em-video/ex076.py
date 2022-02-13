# Lista de Preços com Tupla
'''Crie um programa que tenha uma TUPLA
única com NOMES DE PRODUTOS e seus respectivos
PREÇOS, na sequência. No final, mostre uma listagem
de preços, organizando os dados em forma TABULAR'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('\033[1m''-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # o comando :^40 serve para centralizar o texto em espacos
print('-' * 40)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'\033[m{listagem[posicao]:.<30}', end='')
        # o comando :.<30 serve para fixar o texto à esquerda
        # com mais 30 espaços à direita preenchidos com pontinhos
    else:
        print(f'R${listagem[posicao]:>7.2f}')
        # o comando :>7 serve para fixa o texto à direita
        # o comando .2f serve para formatar em 2 casa decimais
print('\033[1m''-' * 40)
