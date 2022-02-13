def leiaDinheiro(msg):
    válido = False
    while not válido:
        valor = str(input(msg)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print('\033[31m'f'ERRO: \"{valor}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(valor)


'''def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31m''ERRO! Digite um número inteiro válido''\033[m')
        if ok:
            break
    return valor'''


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m''ERRO: por favor, digite um número inteiro válido''\033[m')
            continue    # continue para continuar o while
        except KeyboardInterrupt:
            print('\n\033[31m''Entrada de dados interrompida pelo usuário''\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
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
