def somaImposto(taxaImposto, custo):
    total = (1+ (taxaImposto/100))*custo
    return total

i = float(input('Digite a quantia de imposto sobre vendas(em %): '))
j = float(input('Digite o custo do produto: '))
print(f'O valor total do produto será: {somaImposto(i, j):.2f} reais')