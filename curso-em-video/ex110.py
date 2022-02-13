# Reduzindo ainda mais seu programa
'''Adicione ao módulo moeda.py criado nos exercícios
anteriores, uma função chamada resumo(), que mostre
na tela algumas informações geradas pelas funções que
já temos no módulo criado até aqui'''

from uteis import moeda

p = float(input('\033[1m''Digite o preço: R$ '))
moeda.resumo(p, 80, 35)
