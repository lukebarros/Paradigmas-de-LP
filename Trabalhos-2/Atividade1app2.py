def conversorTurno(turno):
    turno = turno.split(':')[0]
    if int(turno) >= 12:
        turno = 'P.M'
    else:
        turno = 'A.M'
    return turno

def conversorHora(hora):
    m = hora.split(':')
    horadict = {
        1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,
        13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,00:12
        }
    hr = horadict[int(m[0])]
    mins = m[1]
    return(f'{hr}:{mins}')

while True:
    print('-----Conversor 24h para 12h-----\n')
    i = input('Digite a hora em formato 24h para converter(HH:MM): ')
    print(f'São {conversorHora(i)} {conversorTurno(i)}')
    j = input('Deseja converter novamente? (S/N)\n').upper()
    if j == 'S':
        True
    else:
        break