print('\nDigite suas seguintes informações:\n')
nome = input('Nome: ')
idade = input('Idade: ')
sexo = input('Sexo: ')
tel = input('Telefone: ')
if sexo.lower() == 'feminino':
    print(f'\nNome: {nome}\nTelefone: {tel}')
else:
    exit()