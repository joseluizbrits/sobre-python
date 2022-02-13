# Entrada de dados monetários
'''Dentro do pacote uteis que criamos no
ex111, temos um MÓDULO chamado dado. Crie
uma função chamada leiaDinheiro() que seja
capaz de funcionar como a função input(),
mas com uma VALIDAÇÃO DE DADOS para aceitar
apenas valores que sejam MONETÁRIOS'''

from uteis import dado
from uteis import moeda

p = dado.leiaDinheiro('\033[1m''Digite o preço: R$ ')
moeda.resumo(p, 35, 22)
