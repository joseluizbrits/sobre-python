from time import sleep
from atividades.lib.arquivo import *
from atividades.lib.interface import *

arq = 'atividades.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Tarefas', 'Cadastrar Nova Tarefa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivoAtividades(arq)
    elif resposta == 2:
        cabeçalho('NOVA TAREFA')
        disciplina = str(input('\033[1m''Disciplina: ')).upper()
        for n in range(0, 3):
            cadastrar_tarefa(arq, disciplina, tarefa(), prazo(), dificuldade())
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31m''ERRO: Por favor, digite uma opção válida!')
    sleep(2)
