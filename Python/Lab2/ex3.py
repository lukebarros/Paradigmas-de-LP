n = int(input('Número de pessoas: '))
p = float(input('Preço ingresso: '))
s = int(input('Número de sócios presentes: '))
sp = p*s/2
t = n*p + sp
print(f'{t:.2f} reais')
