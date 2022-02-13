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


def lerArquivoAtividades(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31m''Erro ao ler o arquivo!')
    else:
        cabeçalho('TAREFAS')
        c = 4
        n = 1
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[2] = dado[2].replace('\n', '')
            dado[3] = dado[3].replace('\n', '')
            if c % 4 == 0:
                print(f'\033[34m{n}. {dado[0]}\033[m')
                print(f'{dado[1]}  {"":>11} |   PRAZO: {dado[2]}   |   Dificuldade: {dado[3]}')
                print()
                n += 1
            else:
                print(f'{dado[1]}   |   PRAZO: {dado[2]}   |   Dificuldade: {dado[3]}')
                print()
            c += 1
    finally:
        a.close()


def cadastrar_tarefa(arq, disciplina, tarefa, prazo=0, dificuldade='desconhecida'):
    try:
        a = open(arq, 'at')   # 'at' significa append (anexar) text (texto) num arquivo de texto
    except:
        print('\033[31m''Houve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{disciplina}; {tarefa}; {prazo}; {dificuldade}\n')
        except:
            print('\033[31m''Houve um erro na hora de escrever os dados!')
        else:
            print('\033[32m'f'Novo registro de {disciplina} adicionado''\033[m')
            a.close()
