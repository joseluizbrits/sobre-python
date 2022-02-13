import os
carros = []

class Carro:
    nome = ''
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.desligar()

    def info(self):
        print('----------------------------------')
        print(f'Nome.......: {self.nome}')
        print(f'Potência...: {self.pot}')
        print(f'Vel. Máxima: {self.velMax}')
        print(f'Ligado.....: {"Sim" if self.ligado == True else "Não"}')
        print('----------------------------------')


def Menu():
    print('---------------MENU---------------')
    print('1 - Novo Carro')
    print('2 - Informações do Carro')
    print('3 - Excluir Carro')
    print('4 - Ligar Carro')
    print('5 - Desligar Carro')
    print('6 - Listar Carro')
    print('7 - Sair')
    print(f'Quantidade de Carros: {len(carros)}')
    print('----------------------------------')
    opc = int(input('\033[1m''Digite uma opção: \033[m'))
    return opc


def NovoCarro():
    print('----------------------------------')
    n = str(input('Nome do Carro....: '))
    p = int(input('Potência do Carro: '))
    car = Carro(n, p)
    carros.append(car)
    print('\033[32m''Novo carro criado com sucesso\033[m')
    os.system('pause')


def informacoes():
    print('----------------------------------')
    p = 0
    for c in carros:
        print(f'{p} - {c.nome}')
        p += 1
    print('----------------------------------')
    n = int(input('Informe o número do carro que deseja ver as informações: '))
    try:
        carros[n].info()
    except:
        print('\033[31m''Carro não existe na lista''\033[m')
    os.system('pause')


def excluirCarro():
    p = 0
    for c in carros:
        print(f'{p} - {c.nome}')
        p += 1
    n = int(input('Informe o número do carro que deseja excluir: '))
    try:
        del carros[n]
        print('\033[32m''Carro excluído com sucesso''\033[m')
    except:
        print('\033[31m''Carro não existe na lista''\033[m')
    os.system('pause')


def ligarCarro():
    p = 0
    for c in carros:
        print(f'{p} - {c.nome}')
        p += 1
    n = int(input('Informe o número do carro que deseja ligar: '))
    try:
        carros[n].ligar()
        print('\033[32m''Carro ligado com sucesso''\033[m')
    except:
        print('\033[31''Carro não existe na lista''\033[m')
    os.system('pause')

def desligarCarro():
    p = 0
    for c in carros:
        print(f'{p} - {c.nome}')
        p += 1
    n = int(input('\033[1m''Informe o número do carro que deseja desligar: \033[m'))
    try:
        carros[n].desligar()
        print('\033[32m''Carro desligado com sucesso''\033[m')
    except:
        print('\033[31m''Carro não existe na lista''\033[m')
    os.system('pause')


def listarCarros():
    p = 0
    for c in carros:
        print(f'{p} - {c.nome}')
        p += 1
    os.system('pause')


ret = Menu()
while ret < 7:
    if ret == 1:
        NovoCarro()
    elif ret == 2:
        informacoes()
    elif ret == 3:
        excluirCarro()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        listarCarros()
    ret = Menu()

print('-------PROGRAMA FINALIZADO!-------')
