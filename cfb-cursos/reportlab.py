from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)

def criarPDF():
    try:
        cnv = canvas.Canvas(pastaApp + '\\pdf_exemplo.pdf', pagesize=A4)
        cnv.save()
    except:
        messagebox.showerror(title='ERRO', message='Erro ao criar o PDF')
    else:
        messagebox.showinfo(title='PDF', message='PDF criado com sucesso')


app = Tk()
app.title('BLOCO')
app.geometry('600x450')

btn_criarPDF = Button(app, text='Criar PDF', command=criarPDF)
btn_criarPDF.pack(size='left', padx=10)


app.mainloop()
