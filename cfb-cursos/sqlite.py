import sqlite3
from sqlite3 import Error


########## Criar Conexão
def ConexaoBanco():
    caminho = "C:\\Users\\VITOR\\Documents\\BRITS\\Programação\\agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()

vsql = """CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""


def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)


criarTabela(vcon, vsql)

vcon.close()

vsql = """INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
        VALUES('George Clooney', '(21) 97530-2234', 'clooney_bonitao@email.com')"""

def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)


inserir(vcon, vsql)

vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO = 2"

def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro removido')
    except Error as ex:
        print(ex)


deletar(vcon, vsql)

vsql = """UPDATE tb_contatos SET
            T_NOMECONTATO = 'Richard Gere',
            T_TELEFONECONTATO = '(21) 99236-4155',
            T_EMAILCONTATO = 'galanteador_gere@email.com'
        WHERE N_IDCONTATO = 1"""

def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro atualizado')
    except Error as ex:
        print(ex)


atualizar(vcon, vsql)

vsql = "SELECT * FROM tb_contatos WHERE N_IDCONTATO = 1"

def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


res = consulta(vcon, vsql)
for r in res:
    print(r)
