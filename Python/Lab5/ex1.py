from tkinter import *
from tkinter import messagebox

def botao():
    media = (int(vNota1.get()) + int(vNota2.get()))/2
    messagebox.showinfo('MENSAGEM', f'A média do aluno é {media} pontos')
    vMatricula.delete(0,END)
    vDisciplina.delete(0,END)
    vNome.delete(0,END)
    vNota1.delete(0,END)
    vNota2.delete(0,END)
    Entry.focus(vMatricula)

app=Tk()
app.title('Boletim do Aluno')
app.geometry('500x350')
app.configure(background='light blue')

Label(app, text='Matricula:', background='light blue', foreground='midnight blue', anchor=W).place(x=10, y=10, width=200, height=20)
vMatricula = Entry(app)
vMatricula.place(x=70, y=10)
Label(app, text='Nome:', background='light blue', foreground='midnight blue', anchor=W).place(x=10, y=60, width=200, height=20)
vNome = Entry(app)
vNome.place(x=70, y=60)
Label(app, text='Disciplina:', background='light blue', foreground='midnight blue', anchor=W).place(x=10, y=110, width=200, height=20)
vDisciplina = Entry(app)
vDisciplina.place(x=70,y=110)
Label(app, text='Nota 1:', background='light blue', foreground='midnight blue', anchor=W).place(x=10, y=160, width=200, height=20)
vNota1 = Entry(app)
vNota1.place(x=60, y=160)
Label(app, text='Nota 2:', background='light blue', foreground='midnight blue', anchor=W).place(x=10, y=210, width=200, height=20)
vNota2 = Entry(app)
vNota2.place(x=60, y=210)
Button(app, text='Gravar', command=botao).place(x=10, y=250, width=100, height=30)
app.mainloop()