papelaria = [['lapis',2.5],['borracha',0.50],['caneta',5.50],['caderno',25]]
i = input('Digite o produto para saber o preço: ').upper()
if i == 'LAPIS':
    print('Preço do lápis:',papelaria[0][1])
elif i == 'BORRACHA':
    print('Preço da borracha:',papelaria[1][1])
elif i == 'CANETA':
    print('Preço da caneta:',papelaria[2][1])
elif i == 'CADERNO':
    print('Preço do caderno:',papelaria[3][1])
else:
    print('Produto não encontrado.')