distancia = float(input('Digite a distância do veículo (metros): '))
velocidade = float(input('Digite a velocidade do veículo (km/h): '))
si = velocidade/3.6
instante = float(input('Posição para calculo do instante de tempo (metros): '))
calc = (instante - distancia)/si
print(f'\nFunção horária: S = {distancia:.1f} + {si:.1f}t\nInstante de tempo em que o veículo estará em {instante} metros: {calc:.1f} segundos\n')