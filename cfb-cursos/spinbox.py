from tkinter import *

def impValor():
    print(f'Valor: {sb_valores.get()}')


app = Tk()
app.title('BLOCO')
app.geometry('500x300')


sb_valores = Spinbox(app, from_=0, to=10)
sb_valores.pack()

btn_valor = Button(app, text='Imprimir valor', command=impValor)
btn_valor.pack()


app.mainloop()
