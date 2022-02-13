# Funções para votação
'''Crie um programa que tenha uma FUNÇÃO chamada voto()
que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma
pessoa, RETORNANDO um valor LITERAL indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições'''
import datetime


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos:\033[1m NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos:\033[1m VOTO OPCIONAL'
    else:
        return f'Com {idade} anos:\033[1m VOTO OBRIGATÓRIO'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
