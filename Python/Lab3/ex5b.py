papelaria = []
produtos = []

for i in range (4):
    produtos.append(input('Digite um produto para adicionar a lista: '))
    produtos.append(float(input('Digite o preço do produto: ')))
    papelaria.append(produtos[:])
    produtos.clear()
print(papelaria)
