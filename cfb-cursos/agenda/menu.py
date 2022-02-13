from tkinter import *
import os

def semComando():
    print('')


pastaApp = os.path.dirname(__file__)


def novoContato():
    exec(open(pastaApp + "\\formulario.py").read())


app = Tk()
app.title('BLOCO')
app.geometry('500x300')
app.configure(background='#dde')

barraDeMenus = Menu(app)
menuContatos = Menu(barraDeMenus, tearoff=0)
menuContatos.add_command(label='Novo', command=novoContato)
menuContatos.add_command(label='Pesquisar', command=semComando)
menuContatos.add_command(label='Deletar', command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label='Fechar', command=app.quit)
barraDeMenus.add_cascade(label='Contatos', menu=menuContatos)

menuManutencao = Menu(barraDeMenus, tearoff=0)
menuManutencao.add_command(label='Banco de Dados', command=semComando)
barraDeMenus.add_cascade(label='Manutenção', menu=menuManutencao)

menuSobre = Menu(barraDeMenus, tearoff=0)
menuSobre.add_command(label='BLOCO Ventures', command=semComando)
barraDeMenus.add_cascade(label='Sobre', menu=menuSobre)

app.config(menu=barraDeMenus)
app.mainloop()
