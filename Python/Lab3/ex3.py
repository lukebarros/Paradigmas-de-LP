n = 0
for i in range(10):
    j = int(input('Digite um número: '))
    if j % 2 == 0:
        n+=j
print(f'O somatório é: {n}')