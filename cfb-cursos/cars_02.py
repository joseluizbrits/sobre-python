import os

carros = list()


def carrinho(nome_carro='<Error!!, Escreva Um Nome Valido De Um Carro>'):
    print(f'\033[31m{nome_carro}\033[m')


def inteiro(txt):
    while True:
        try:
            potência_carro = int(input(txt))
        except(ValueError, TypeError):
            print('\033[1;31m<Error!!, Digite Uma Potência Válida Do     Carro>\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m<Error!!, Digite Uma Potência Válida Do     Carro>\033[m')
            return 0
        else:
            return potência_carro


def cadastro(opção='<Error!!, Digite Apenas As Opções Do Menu>'):
    print(f'\033[1;31m{opção}\033[m')


class Carro:
    nome = ''
    potência = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, potência):
        self.nome = nome
        self.potência = potência
        self.velMax = int(potência) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print('\nNome.......: ' + self.nome)
        print('Potência...: ' + str(self.potência))
        print('Vel.Maxima.: ' + str(self.velMax))
        print('Ligado.....: ' + ('Sim' if self.ligado == True else 'Não'))


def menu():
    print('\n')
    os.system("cls") or None
    print('-' * 43)
    print(f'\033[1;3;37m{f"Menu De Opções":^43}\033[m')
    print('-' * 43)
    print(' \033[1;32m1\033[m - \033[1;36mNovo Carro\033[m')
    print(' \033[1;32m2\033[m - \033[1;36mInformações Do Carro\033[m')
    print(' \033[1;32m3\033[m - \033[1;36mExcluir Carro\033[m')
    print(' \033[1;32m4\033[m - \033[1;36mLigar Carro\033[m')
    print(' \033[1;32m5\033[m - \033[1;36mDesligar Carro\033[m')
    print(' \033[1;32m6\033[m - \033[1;36mListar Carro\033[m')
    print(' \033[1;32m7\033[m - \033[1;31mSair\033[m')
    print(' \033[1;32m8\033[m - \033[1;36mQuantidade De Carros:\033[m ' + str(len(carros)))
    print('-' * 43)

    while True:
        opção = input(f'\n\033[1m{">> Digite Uma Opção: "}')
        if opção not in '1234567':
            cadastro(opção='<Error!!, Digite Apenas As Opções Do Menu>')
        else:
            break
    return opção


def Novo_Carro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 1 -----":^43}\033[m')
    print('=' * 43)
    while True:
        nome_carro = input(f'\n\033[1m{">> Nome Do Carro: "}')
        if nome_carro.isnumeric() or nome_carro.strip() == '' or len(nome_carro) < 6:
            carrinho(nome_carro='<Error!!, Escreva Um Nome Valido De Um      Carro>')
        else:
            break
    potência_carro = inteiro(f'\n\033[1m{">> Potência Do Carro: "}')
    car = Carro(nome_carro, potência_carro)
    carros.append(car)
    print('=' * 43)
    print(f'\033[1;32m{"Novo Carro Adicionado Com Sucesso":^43}\033[m')
    print('=' * 43)
    os.system('pause')


def Informações():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 2 -----":^43}\033[m')
    print('=' * 43)
    nome_carro = input('\n\033[1m{}'.format(' Informe O Número Do Carro Que Desseja Ver  As Informações: ')).strip()
    try:
        carros[int(nome_carro)].info()
    except:
        print('=' * 43)
        print(f'\033[1;31m{"<Error!!, Carro Não Existe Na Lista>":^43}\033[m')
        print('=' * 43)
    os.system('pause')


def excluirCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 3 -----":^43}\033[m')
    print('=' * 43)
    nome_carro = input('\n\033[1m{}'.format(' Informe O Número Do Carro Que Desseja      Excluir: '))
    try:
        del carros[int(nome_carro)]
        print('=' * 43)
        print(f'\033[1;32m{"<Parabéns!!, Carro Excluído Com Sucesso>"}\033[m')
        print('=' * 43)
    except:
        print('=' * 43)
        print(f'\033[1;31m{"<Error!!, Carro Não Existe Na Lista>":^43}\033[m')
        print('=' * 43)
    os.system('pause')


def ligarCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 4 -----":^43}\033[m')
    print('=' * 43)
    nome_carro = input('\n\033[1m{}'.format(' Informe O Número Do Carro Que Desseja      Ligar: '))
    try:
        carros[int(nome_carro)].ligar()
        print('=' * 43)
        print(f'\033[1;32m{"<Carro Ligado Com Sucesso>":^43}\033[m')
        print('=' * 43)
    except:
        print('=' * 43)
        print(f'\033[1;31m{"<Error!!, Carro Não Existe Na Lista>":^43}\033[m')
        print('=' * 43)
    os.system('pause')


def desligarCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 5 -----":^43}\033[m')
    print('=' * 43)
    nome_carro = input('\n\033[1m{}'.format(' Informe O Número Do Carro Que Desseja      Desligar: '))
    try:
        carros[int(nome_carro)].desligar()
        print('=' * 43)
        print(f'\033[1;32m{"<Carro Desligado Com Sucesso>":^43}\033[m')
        print('=' * 43)
    except:
        print('=' * 43)
        print(f'\033[1;31m{"<Error!!, Carro Não Existe Na Lista>":^43}\033[m')
        print('=' * 43)
    os.system('pause')


def listarCarros():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print(f'\033[1;3;37m{f"----- Opção 6 -----":^43}\033[m')
    print('=' * 43)
    posição = 0
    for um, dois in enumerate(carros):
        print(f'\n\033[1;31m {um + 1}° Carro Adicionado\033[m')
        print(str() + " - " + dois.nome)
        print('-' * 43)
        posição += 1
    os.system('pause')


retorno = menu()
while retorno < '7':

    if retorno == '1':
        Novo_Carro()

    elif retorno == '2':
        Informações()

    elif retorno == '3':
        excluirCarro()

    elif retorno == '4':
        ligarCarro()

    elif retorno == '5':
        desligarCarro()

    elif retorno == '6':
        listarCarros()
    retorno = menu()

os.system("cls") or None
print('\n\033[1m------ Programa Finalizado ------\033[m')
print('\033[1m  ------ Obrigado... Volte Sempre ------\033[m')
