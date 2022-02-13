from tkinter import *

app = Tk()
app.title('BLOCO')
app.geometry('500x300')

lb_dados = Label(app, text='Dados')
lb_nome = Label(app, text='Digite o seu nome')
lb_idade = Label(app, text='Informe a sua idade')

et_nome = Entry(app)
et_idade = Entry(app)

btn = Button(app, text='BUTTON')

lb_dados.grid(row=0, column=0, columnspan=2, pady=15)  # columnspan=2 - mesclar duas colunas

lb_nome.grid(row=1, column=0, sticky='w')   # sticky='w' - posição a oeste (west) da grade
et_nome.grid(row=2, column=0, padx=5)    # padx - espaço em x, pady - espaço em y

lb_idade.grid(row=1, column=1, sticky='w')  # n - north, s - south, e - east, w - west
et_idade.grid(row=2, column=1, padx=5)


app.mainloop()
