# Formatando Moedas em Python
'''Adapte o código do ex107, criando uma função
adcional chamada moeda() que consiga mostrar os
valores como um valor monetário formatado'''

from uteis import moeda

p = float(input('\033[1m''Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
