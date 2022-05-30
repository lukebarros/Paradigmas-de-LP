from random import randint
from time import sleep

carioca = ['FLUMINENSE','FLAMENGO','VASCO','BOTAFOGO']

def partida(time1, time2):
    placarCasa1 = randint(0,3)
    placarFora1 = randint(0,3)
    print('\nComeça o primeiro tempo....\n')
    sleep(2)
    print('Placar atual 0 - 0')
    sleep(5)
    print(f'Termina o primeiro tempo, Placar atual: {time1:.3s} {placarCasa1} - {placarFora1} {time2:.3s}')
    sleep(2)
    print('Começa o Segundo tempo')
    sleep(5)
    placarCasa2 = placarCasa1+randint(0,2)
    placarFora2 = placarFora1+randint(0,2)
    print(f'Fim de jogo, Placar: {time1:.3s} {placarCasa2} - {placarFora2} {time2:.3s}')


i = int(input('CAMPEONATO CARIOCA 2021\n\nEscolha o time da casa:\n[1]Fluminense\n[2]Flamengo\n[3]Vasco\n[4]Botafogo\n\n'))
j = int(input('\nCAMPEONATO CARIOCA 2021\n\nEscolha o time de fora:\n[1]Fluminense\n[2]Flamengo\n[3]Vasco\n[4]Botafogo\n\n'))

timeCasa = carioca[i-1]
timeFora = carioca[j-1]

partida(timeCasa, timeFora)


