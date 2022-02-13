from tkinter import *

app = Tk()
app.title('BLOCO')
app.geometry('500x300')


quadro = Frame(app, borderwidth=1, relief='solid', background='#101')
quadro.place(x=10, y=10, width=300, height=100)

label = Label(quadro, text='BLOCO Ventures', background='#515', foreground='#fff', font=('Times New Roman', 25))
label.pack(side=LEFT, fill=X, expand=TRUE)


app.mainloop()
