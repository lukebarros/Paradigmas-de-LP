print('Calculo de Juros Simples:\n\n')
capital = float(input('Digite o capital: '))
taxa = float(input('Taxa de Juros: '))
temptaxa = input('Taxa ao mês, ao ano ou ao dia? ')
tempo = float(input('Tempo de empréstimo (em anos): '))
if temptaxa == 'mês' or temptaxa == 'mes':
    tempo*= 12
elif temptaxa == 'dia':
    tempo*= 365
juros = capital * taxa/100 * tempo
print(f'Resultado: {juros:.2f} reais')