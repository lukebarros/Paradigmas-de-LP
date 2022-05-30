from random import choice
from time import sleep

def randpalavra():
    p = ['carro', 'bicicleta', 'celular']
    pran = choice(p)
    return pran


print('Jogo da Advinhação\n\nAdvinhe a palavra em três tentativas baseando-se nas pistas dadas\n')
sleep(2)

pran = randpalavra()
if pran == 'carro':
    for k in range(1,4):
        i = input('Possui portas, rodas e pode ser utilizado para corridas\n').lower()
        if i == pran:
            print(f'Parabéns você acertou, a palavra era "{pran}"')
            break
        elif k >= 3:
            print(f'Você errou, a palavra era "{pran}"')
            break
        else:
            print('Tente Novamente.')
elif pran == 'bicicleta':
    for k in range(1,4):
        i = input('Possui rodas, marcha e pode ser utilizado para corridas\n').lower()
        if i == pran:
            print(f'Parabéns você acertou, a palavra era "{pran}"')
            break
        elif k >= 3:
                print(f'Você errou, a palavra era "{pran}"')
                break
        else:
            print('Tente Novamente.')
else:
    for k in range(1,4):
        i = input('Possui display, é capaz de acessar a internet e pode ser utilizado para jogos\n')
        if i == pran:
            print(f'Parabéns você acertou, a palavra era "{pran}"')
            break
        elif k >= 3:
                print(f'Você errou, a palavra era "{pran}"')
                break
        else:
            print('Tente Novamente.')
