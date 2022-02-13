from tkinter import *

def imprimirEsporte():
    print(f'Esporte: {lb_esportes.get(ACTIVE)}')


def addEsporte():
    lb_esportes.insert(END, vnovoesporte.get())   # END - final da lista


app = Tk()
app.title('BLOCO')
app.geometry('500x300')

listaEsportes = ['Futebol', 'Vôlei', 'Basquete']

lb_esportes = Listbox(app)
for esportes in listaEsportes:
    lb_esportes.insert(END, esportes)   # END - final da lista
lb_esportes.pack()

btn_esporte = Button(app, text='Imprimir esporte', command=imprimirEsporte)
btn_esporte.pack()

vnovoesporte = Entry(app)
vnovoesporte.pack()

btn_inserirEsporte = Button(app, text='Adicionar esporte', command=addEsporte)
btn_inserirEsporte.pack()


app.mainloop()
