# Exercitando módulos em Python
'''Crie um módulo chamado moeda.py que tenha
as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também m programa que
IMPORTE esse módulo e use algumas dessas funções'''

from uteis import moeda

p = float(input('\033[1m''Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
