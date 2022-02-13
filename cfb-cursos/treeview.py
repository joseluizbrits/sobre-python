from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if vid.get() == '' or vnome.get() == '' or vfone.get() == '':
        messagebox.showerror(title='ERRO', message='Por favor. Digite todos os dados.')
        return
    tv.insert('', 'end', values=(vid.get(), vnome.get(), vfone.get()))
    vid.delete(0, END)
    vnome.delete(0, END)
    vfone.delete(0, END)
    vid.focus()             # Colocar o cursor no Entry do ID


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


app = Tk()
app.title('BLOCO')
app.geometry('500x300')


lbid = Label(app, text='ID', anchor=W)
vid = Entry(app)

lbnome = Label(app, text='Nome', anchor=W)
vnome = Entry(app)

lbfone = Label(app, text='Fone', anchor=W)
vfone = Entry(app)

tv = ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)  # show='headings' - mostrar cabeçalho
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

btn_inserir = Button(app, text='Inserir', command=inserir)
btn_deletar = Button(app, text='Deletar', command=deletar)
btn_obter = Button(app, text='Obter', command=obter)

lbid.grid(column=0, row=0, stick='w')
vid.grid(row=1, column=0)

lbnome.grid(row=0, column=1, stick='w')
vnome.grid(row=1, column=1)

lbfone.grid(row=0, column=2, stick='w')
vfone.grid(row=1, column=2, stick='w')

tv.grid(row=3, column=0, columnspan=3, pady=5)

btn_inserir.grid(row=4, column=0, stick='w')
btn_deletar.grid(row=4, column=1, stick='w')
btn_obter.grid(row=4, column=2, stick='w')


app.mainloop()
