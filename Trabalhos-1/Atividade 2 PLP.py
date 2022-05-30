i = 1
while i != 2:
    print('Calculo de Area')
    escolha = input('\n1-Triangulo\n2-Quadrado\n3-Losango\n4-Retangulo\n5-Trapezio\n6-Circulo\n\nEscolha a forma para calculo: ')
    if escolha == '1':
        baseTriangulo = float(input('\nBase do triangulo: '))
        alturaTriangulo = float(input('Altura do triangulo: '))
        areaTriangulo = (baseTriangulo * alturaTriangulo)/2
        print('\nArea do triangulo: %.2f'%areaTriangulo)
    elif escolha == '2':
        ladoQuadrado = float(input('\nLado do Quadrado: '))
        areaQuadrado = ladoQuadrado**2
        print('\nArea do Quadrado: %.2f'%areaQuadrado)
    elif escolha == '3':
        diagMenLosango = float(input('\nDiagonal menor do losango: '))
        diagMaiLosango = float(input('Diagonal maior do losango: '))
        areaLosango = (diagMaiLosango * diagMenLosango)/2
        print('\nArea do Losango: %.2f'%areaLosango)
    elif escolha == '4':
        baseRetangulo = float(input('\nBase retangulo: '))
        alturaRetangulo = float(input('Altura retangulo: '))
        areaRetangulo = baseRetangulo * alturaRetangulo
        print('\nArea do Retangulo: %.2f'%areaRetangulo)
    elif escolha == '5':
        baseMaiTrapez = float(input('\nBase maior trapezio: '))
        baseMenTrapez = float(input('Base menor trapezio: '))
        alturaTrapez = float(input('Altura trapezio: '))
        areaTrapez = ((baseMaiTrapez + baseMenTrapez) * alturaTrapez)/2
        print('\nArea do Trapezio: %.2f'%areaTrapez)
    elif escolha == '6':
        pi = 3.14
        raio = float(input('\nRaio do Circulo: '))
        areaCirculo = pi * raio**2
        print('\nArea do Circulo: %.2f'%areaCirculo)
    else:
        print('\nOpção inválida!')   
    print('\n1- Continuar\n2- Sair')
    i = int(input())