# Funções aprofundadas em Python
'''Reescreva a função leiaint() que fizemos no
ex104 (que está no pacote uteis, módulo dados),
incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também
uma função leiafloat() com a mesma funcionalidade'''

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m''ERRO: por favor, digite um número inteiro válido''\033[m')
            continue    # continue para continuar o while
        except KeyboardInterrupt:
            print('\n\033[31m''O usuário decidiu não digitar esse número''\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m''ERRO: por favor, digite um número inteiro válido''\033[m')
            continue    # continue para continuar o while
        except KeyboardInterrupt:
            print('\n\033[31m''O usuário decidiu não digitar esse número''\033[m')
            return 0
        else:
            return n


n1 = leiaint('\033[1m''Digite um Número Inteiro: ')
n2 = leiafloat('\033[1m''Digite um Número Real: ')
print(f'O valor do Número Inteiro digitado foi {n1} e do Número Real foi {n2}')
