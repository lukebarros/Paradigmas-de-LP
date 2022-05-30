nome = input('Escreva seu nome: ')
civil = input('Escreva a letra inicial de seu estado civil:\nS, C, D, V ou O: ').capitalize()
if civil == 'S':
    print('Solteiro')
elif civil == 'C':
    print('Casado')
elif civil == 'D':
    print('Divorciado')
elif civil == 'V':
    print('Viúvo')
else:
    print('Outros')



