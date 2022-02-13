# Função que calcula área
'''Faça um programa que tenha uma FUNÇÃO chamada
area(), que receba as dimensões de um terreno
retangular (LARGURA e COMPRIMENTO) e mostre a
ÁREA DO TERRENO'''

def area(larg, comp):
    a = larg * comp
    print(f'A areá de um terreno {larg}x{comp} é de {a}m²')


# Programa Principal
print('\033[1m''Controle de Terrenos''\033[m')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
