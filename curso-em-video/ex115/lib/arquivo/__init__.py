from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # open é para abrir um arquivo e 'rt'
        a.close()             # significa read (ler) um text (texto)
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')   # 'wt+' significa write (escrever) um text (texto) e o
        a.close()               # + é para criar um arquivo de texo, caso ele não exista
    except:
        print('\033[31m''Houve um erro na criação do arquivo!\033[m')
    else:
        print('\033[32m'f'Arquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31m''Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')   # 'at' significa append (anexar) text (texto) num arquivo de texto
    except:
        print('\033[31m''Houve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('\033[31m''Houve um erro na hora de escrever os dados!')
        else:
            print('\033[32m'f'Novo registro de {nome} adicionado')
            a.close()
