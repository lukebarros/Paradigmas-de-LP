from tkinter import *
import math

# A biblioteca 'math' é apontada como em 'não uso' pelo ide, mas está sendo usada dentro
# de strings para que a função 'eval' a interprete 

calc = Tk()
calc.geometry("312x435") 
calc.resizable(0, 0)  # Janela sem redimensionamento
calc.title("Calculadora - Lucas Barros")

# 'btn_click' envia dados ao campo de escrita(input_field) para que estes
# sejam interpretados pelo 'bt_igual' 

def btn_click(item):
    global expression
    if item == "sqrt":
        expression = f'math.sqrt(float({expression}))'
        input_text.set(expression)
    elif item == "Sen":
        expression = f'math.sin(float({expression}))'
        input_text.set(expression)
    elif item == "Cos":
        expression = f'math.cos(float({expression}))'
        input_text.set(expression)
    elif item == "Tan":
        expression = f'math.tan(float({expression}))'
        input_text.set(expression)
    else:
        expression += str(item)
        input_text.set(expression)

# 'bt_limpa' limpa o campo de escrita

def bt_limpa(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_igual' Realiza o calculo presente no campo de escrita
 
def bt_igual():
    global expression
    result = str(eval(expression)) # Função 'eval' para interpretar a string gerada no campo de escrita 
    input_text.set(result)
    expression = ""
 
expression = ""
 
# Campo de escrita recebendo 'StringVar()' do tkinter

input_text = StringVar()
 
# Criação do frame para o campo de escrita
 
input_frame = Frame(calc, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
# Campo de escrita dentro do frame
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # Padding interno para aumentar a altura do campo de escrita
 
# Frame para os botões abaixo do campo de escrita
 
btns_frame = Frame(calc, width=312, height=400, bg="grey")
 
btns_frame.pack()
 
# Linha 1
 
limpa = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_limpa()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# Linha 2
 
sete = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
oito = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nove = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiplica = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# Linha 3
 
quatro = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
cinco = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
seis = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
menos = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# Linha 4
 
um = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
dois = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
tres = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
soma = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# Linha 5
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#8cd3ff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
virgula = Button(btns_frame, text = ",", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
potencia = Button(btns_frame, text = "x^y", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("**")).grid(row = 4, column = 3, padx = 1, pady = 1)

# Linha 6

raiz = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: btn_click("sqrt")).grid(row = 5, column = 0, padx = 1, pady = 1)

seno = Button(btns_frame, text = "Sen", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("Sen")).grid(row = 5, column = 1, padx = 1, pady = 1)
 
cosseno = Button(btns_frame, text = "Cos", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("Cos")).grid(row = 5, column = 2, padx = 1, pady = 1)

tangente = Button(btns_frame, text = "Tan", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("Tan")).grid(row = 5, column = 3, padx = 1, pady = 1)

# Linha 7

igual = Button(btns_frame, text = "=", fg = "black", width = 43, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_igual()).grid(row = 6, column = 0, columnspan = 4, padx = 1, pady = 1)

calc.mainloop()