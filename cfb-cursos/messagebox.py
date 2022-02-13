from tkinter import *
from tkinter import messagebox

def mostrarMsg(tipomsg, msg):
    if tipomsg == '1':
        messagebox.showinfo(title='BLOCO', message='BLOCO Ventures')
    elif tipomsg == '2':
        messagebox.showwarning(title='BLOCO', message='BLOCO Ventures')
    elif tipomsg == '3':
        messagebox.showerror(title='BLOCO', message='BLOCO Ventures')


def resetarTB():
    res = messagebox.askyesno('Resetar', 'Confirma reset do Text Box?')
    if res == True:
        tb_num.delete(0, END)
        tb_num.insert(0, '1')


vmsg = 'BLOCO Ventures'

app = Tk()
app.title('BLOCO')
app.geometry('500x300')

vnum_cxtexto = StringVar()

Label(app, text='Tipo de cx(1, 2 ou 3)').pack()
tb_num = Entry(app, textvariable=vnum_cxtexto)
vnum_cxtexto.set('1')
tb_num.pack()

btn_msg = Button(app, text='Mostrar mensagem', command=lambda: mostrarMsg(vnum_cxtexto.get(), vmsg))
btn_msg.pack()

btn_reset = Button(app, text='Resetar Text Box', command=resetarTB())
btn_reset.pack()

app.mainloop()
