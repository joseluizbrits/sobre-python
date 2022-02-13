import datetime

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1:33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[1:32m''Sua opção: \033[m')
    return opc


def tarefa():
    c = 0
    while c < 3:
        print('\033[1:34m[1]\033[m - Fórum Temático Avaliativo')
        print('\033[1:34m[2]\033[m - Atividade Individual Avaliativa (A1)')
        print('\033[1:34m[3]\033[m - Atividade Individual Avaliativa (A2)')
        try:
            print(linha())
            opc = int(input('\033[1:32m''Opção: \033[m'))
            print(linha())
        except:
            print('\033[31m''Digite uma opção válidada\033[m')
        else:
            if opc == 1:
                tarefa = 'Fórum Temático Avaliativo'
                return tarefa
            elif opc == 2:
                tarefa = 'Atividade Individual Avaliativa (A1)'
                return tarefa
            elif opc == 3:
                tarefa = 'Atividade Individual Avaliativa (A2)'
                return tarefa
        c += 1


def prazo():
    print('\033[1m''PRAZO''\033[m')
    data = {'dia': leiaint('Dia: '), 'mes': leiaint('Mês: '), 'ano': leiaint('Ano: ')}
    prazo = f'{data["dia"]}/{data["mes"]}/{data["ano"]}'
    return prazo


def dificuldade():
    print(linha())
    print('\033[1m''Dificuldade''\033[m')
    print('\033[1:34m[1]\033[m - \033[32m''Baixa''\033[m')
    print('\033[1:34m[2]\033[m - \033[33m''Média''\033[m')
    print('\033[1:34m[3]\033[m - \033[31m''Alta''\033[m')
    print(linha())
    opc = leiaint('\033[1:32m''Opção: \033[m')
    print(linha())
    if opc == 1:
        dif = '\033[32m''Baixa''\033[m'
        return dif
    elif opc == 2:
        dif = '\033[33m''Média''\033[m'
        return dif
    elif opc == 3:
        dif = '\033[31m''Alta''\033[m'
        return dif
