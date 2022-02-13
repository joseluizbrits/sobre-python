from tkinter import *
from tkinter import ttk

app = Tk()
app.title('BLOCO')
app.geometry('500x300')

nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=500, height=300)

aba1 = Frame(nb)
aba2 = Frame(nb)

nb.add(aba1, text='Arquivo')
nb.add(aba2, text='Dados')


app.mainloop()
