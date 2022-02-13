import sqlite3
from sqlite3 import Error
from os import system

def ConexaoBanco():
    caminho = "C:\\Users\\VITOR\\Documents\\BRITS\\Programação\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    else:
        print('\033[32m''Operação realizada com sucesso''\033[m')


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


def menuPrincipal():
    print('1 - Inserir novos registros')
    print('2 - Deletar Registro')
    print('3 - Atualizar Registro')
    print('4 - Consultar ID')
    print('5 - Consultar nomes')
    print('6 - Sair')


def menuInserir():
    vnome = str(input('Digite o nome: '))
    vtelefone = str(input('Digite o telefone: '))
    vemail = str(input('Digite o e-mail: '))
    vsql = f"SELECT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('{vnome}', '{vtelefone}', '{vemail}')"
    vcon = ConexaoBanco()
    query(vcon, vsql)
    vcon.close()


def menuDeletar():
    vid = str(input('Digite o ID do registro a ser deletado: '))
    vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO = {vid}"
    vcon = ConexaoBanco()
    query(vcon, vsql)
    vcon.close()


def menuAtualizar():
    vid = str(input('Digite o ID do registro a ser alterado: '))
    vcon = ConexaoBanco()
    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {vid}")
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = str(input('Digite o nome: '))
    vtelefone = str(input('Digite o telefone: '))
    vemail = str(input('Digite o e-mail: '))
    if len(rnome) == 0:
        vnome = rnome
    if len(rtelefone) == 0:
        vtelefone = rtelefone
    if len(remail) == 0:
        vemail = remail
    vsql = f"UPDATE tb_contatos SET T_NOMECONTATO = '{vnome}', T_TELEFONECONTATO = '{vtelefone}', T_EMAILCONTATO = '{vemail}' WHERE N_IDCONTATO = {vid}"
    query(vcon, vsql)
    vcon.close()


def menuConsultarID():
    vsql = "SELECT * FROM  tb_contatos"
    vcon = ConexaoBanco()
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f'ID:{r[0]:_<3} Nome:{r[1]:_<30} Telefone:{r[2]:_<14} E-mail:{r[3]:_<30}')
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            system('pause')
    print('Fim da lista')
    vcon.close()
    system('pause')


def menuConsultarNomes():
    vnome = str(input('Digite o nome: '))
    vsql = f"SELECT * FROM  tb_contatos WHERE T_NOMECONTATO LIKE '%{vnome}%'"
    vcon = ConexaoBanco()
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f'ID:{r[0]:_<3} Nome:{r[1]:_<30} Telefone:{r[2]:_<14} E-mail:{r[3]:_<30}')
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            system('pause')
    print('Fim da lista')
    vcon.close()
    system('pause')


opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input('Digite um opção: '))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarID()
    elif opc == 5:
        menuConsultarNomes()
    elif opc == 6:
        print('\033[1m''PROGRAMA FINALIZADO''\033[m')
    else:
        print('\033[31m''Opção inválida''\033[m')
        system('pause')
