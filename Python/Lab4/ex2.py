n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
minmax = [n1,n2,n3]
minmax.sort(reverse=True)

media = (n1+n2+n3)/3
soma = n1+n2+n3
produto = n1*n2*n3
maior = minmax[0]
menor = minmax[2]

print(f'\nMédia: {media}\nSoma: {soma}\nProduto: {produto}\nMaior numero: {maior}\nMenor numero: {menor}')

