n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
ordemlist = [n1,n2,n3]
ordemlist.sort(reverse=True)
print(f'Maior: {ordemlist[0]}\nMediano: {ordemlist[1]}\nMenor: {ordemlist[2]}')