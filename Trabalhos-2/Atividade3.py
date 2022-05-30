from tkinter import *
from tkinter import messagebox
import os

c = os.path.dirname(__file__)
arqlogin = c+'\\login.txt'

def btn_click(): # Realiza leitura dos dados dentro do arquivo "login.txt" para autenticação
    with open(arqlogin,'r') as lg:
        lines = lg.readlines()
        if login.get() == lines[0].rstrip() and senha.get() == lines[1].rstrip():
            messagebox.showinfo('Mensagem', 'Usuário autenticado!')
            return True
        else: 
            messagebox.showerror('Erro', 'Falha na autenticação, login e/ou senha incorretos')
            return False


app = Tk()
app.title('Autenticação')
app.geometry('400x400')
app.resizable(0,0)
app.configure(bg='light blue')

login = StringVar()
senha = StringVar()

Label(app,text='Insira suas credenciais abaixo\n\n', bg='light blue').pack()
loginlabel = Label(app, text='Nome de usuário*',bg='light blue', fg='#000',anchor=W)
loginlabel.pack()
Entry(app, textvariable=login, font=('arial', 10, 'bold'), width=20, justify=CENTER).pack(ipady=2)
senhalabel = Label(app, text='\n\nSenha*', bg='light blue', fg='#000',anchor=W)
senhalabel.pack()
Entry(app, textvariable=senha, show='*', width=20, justify=CENTER).pack(ipady=2)
Button(app, text='Entrar', width=10, command=btn_click).pack(pady=10)
app.mainloop()