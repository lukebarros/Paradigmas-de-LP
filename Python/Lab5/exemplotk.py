from tkinter import *
from tkinter import messagebox
import os

c = os.path.dirname(__file__)
arqtext =   c+'\\dados.txt'

def botao():
    arquivo = open(arqtext, 'a')
    arquivo.write('\nNome.......:%s'%vnome.get())
    arquivo.write('\nTelefone...:%s'%vtelefone.get())
    arquivo.write('\nE-mail......:%s'%vemail.get())
    arquivo.write('\nObservação:%s'%vobs.get(1.0,END))
    arquivo.write('\n')
    arquivo.close()
    messagebox.showinfo('MENSAGEM IMPORTANTE', 'Informações gravadas com sucesso!')
    vnome.delete(0,END)
    vtelefone.delete(0,END)
    vemail.delete(0,END)
    vobs.delete(1.0,END)
    Entry.focus(vnome)

app=Tk()
app.title('Curso de Python')
app.geometry('500x350')
app.configure(background='light grey')

Label(app, text='Nome', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=10, width=200, height=20)
vnome = Entry(app)
vnome.place(x=10, y=30)
Label(app, text='Telefone', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=60, width=200, height=20)
vtelefone = Entry(app)
vtelefone.place(x=10,y=80)
Label(app, text='E-mail', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=110, width=200, height=20)
vemail = Entry(app)
vemail.place(x=10, y=130)
Label(app, text='Observações', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=160, width=200, height=20)
vobs = Text(app)
vobs.place(x=10, y=190, width=300, height=80)
Button(app, text='Gravar', command=botao).place(x=10, y=290, width=100, height=30)
app.mainloop()