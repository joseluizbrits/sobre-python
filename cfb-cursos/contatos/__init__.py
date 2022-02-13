from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from uteis.contatos import banco

def popular():
    tv.delete(*tv.get_children())       # get_children() pega os "filhos" do Treeview
    vquery = 'SELECT * FROM tb_nomes order by ID'       # seleciona tudo, ordenando pelo ID
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values=i)

def inserir():
    if vnome.get() == '' or vfone.get() == '':
        messagebox.showerror(title='ERRO', message='Por favor. Digite todos os dados.')
        return
    try:
        vquery = f"INSERT INTO tb_nomes (nome, fone) VALUES ('{vnome.get()}', '{vfone.get()}')"
        banco.dml(vquery)
    except:
        messagebox.showerror(title='ERRO', message='Erro ao inserir')
        return
    popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vnome.focus()          # Colocar o cursor no Entry do ID


def deletar():
    try:
        itemSelecionado = tv.selection()[0]     # selection() retorna uma tupla
        tv.delete(itemSelecionado)
    except:
        messagebox.showerror(title='ERRO', message='Por favor. Selecione um elemento a ser deletado.')


def obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, 'values')    # item() também retorna uma tupla
        print(f'ID......: {valores[0]}')
        print(f'Nome....: {valores[1]}')
        print(f'Telefone: {valores[2]}')
    except:
        messagebox.showerror(title='ERRO', message='Por favor. Selecione um elemento a ser deletado.')


def pesquisar():
    tv.delete(*tv.get_children())
    vquery = f"SELECT * FROM tb_nomes WHERE nome LIKE '%{vnomepesquisar.get()}%' order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values=i)


app = Tk()
app.title('BLOCO')
app.geometry('600x450')


################ QUADRO CONTATOS ################

quadroGrid = LabelFrame(app, text='Contatos')
quadroGrid.pack(fill='both', expand='yes', padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
tv.pack()
popular()


################ QUADRO INSERIR ################

quadroInserir = LabelFrame(app, text='Inserir Novos Contatos')
quadroInserir.pack(fill='both', expand='yes', padx=10, pady=10)

lbnome = Label(quadroInserir, text='Nome')
lbnome.pack(side='left')
vnome = Entry(quadroInserir)
vnome.pack(side='left', padx=10)
lbfone = Label(quadroInserir, text='Fone')
lbfone.pack(side='left')
vfone = Entry(quadroInserir)
vfone.pack(side='left', padx=10)
btn_inserir = Button(quadroInserir, text='Inserir', command=inserir)
btn_inserir.pack(side='left', padx=10)


################ QUADRO PESQUISAR ################

quadroPesquisar = LabelFrame(app, text='Pesquisar Contatos')
quadroPesquisar.pack(fill='both', expand='yes', padx=10, pady=10)

lbid = Label(quadroPesquisar, text='Nome')
lbid.pack(side='left')
vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side='left', padx=10)
btn_pesquisar = Button(quadroPesquisar, text='Pesquisar', command=pesquisar)
btn_pesquisar.pack(side='left', padx=10)
btn_todos = Button(quadroPesquisar, text='Mostrar Todos', command=popular)
btn_todos.pack(side='left', padx=10)


app.mainloop()
