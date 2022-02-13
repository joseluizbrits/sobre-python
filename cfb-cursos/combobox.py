from tkinter import *
from tkinter import ttk

def imprimirEsporte():
    ve = cb_esportes.get()
    print(f'Esporte: {ve}')


app = Tk()
app.title('BLOCO')
app.geometry('500x300')


listaEsportes = ['Futebol', 'Vôlei', 'Basquete']

lb_esportes = Label(app, text='Esportes')
lb_esportes.pack()

cb_esportes = ttk.Combobox(app, values=listaEsportes)
cb_esportes.set('Futebol')  # set('Futebol') para definir o Futebol como padrão
cb_esportes.pack()

btn_esportes = Button(app, text='Esporte selecionado', command=imprimirEsporte)
btn_esportes.pack()


app.mainloop()
