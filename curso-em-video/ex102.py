# Função para Fatorial
'''Crie um programa que tenha uma FUNÇÃO
fatorial() que receba dois parâmetros: o
primeiro que indique o NÚMERO a calcular
e o outro chamado SHOW, que será um valor
LÓGICO (OPCIONAL) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial'''

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: o valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
num = int(input('\033[1m''Qual número você pretende calcular o fatorial? '))
mostrar = str(input('Você (deseja visualizar o cálculo? [S/N] ')).upper()[0]
if mostrar in 'S':
    print(fatorial(num, show=True))
if mostrar in 'N':
    print(fatorial(num, show=False))
