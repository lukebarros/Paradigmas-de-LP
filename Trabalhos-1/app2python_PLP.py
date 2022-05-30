from time import time
t1 = time()
for i in range(1001): 
    print(i)
t2 = time()
diff = (t2-t1)*1000
print(f'Tempo de execução: {diff:.2f} ms')