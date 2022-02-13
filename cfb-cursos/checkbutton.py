from tkinter import *

app = Tk()
app.title('BLOCO')
app.geometry('500x300')


vfutebol = IntVar()
vvolei = IntVar()
vbasquete = IntVar()

quadro = Frame(app, borderwidth=1, relief='solid')
quadro.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(quadro, text='Futebol', variable=vfutebol, onvalue=1, offvalue=0)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(quadro, text='Vôlei', variable=vvolei, onvalue=1, offvalue=0)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(quadro, text='Basquete', variable=vbasquete, onvalue=1, offvalue=0)
cb_basquete.pack(side=LEFT)


app.mainloop()
