import random

matriz = []
x = random.randint(0,20)

for i in range(5):
    linha = []
    for j in range(5):
        linha += [random.randint(0,20)]
    matriz += [linha]


for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])
v = 0
for i in range(5):
    for j in range(5):
        if x == matriz[i][j]:
            print(f'O nº {x} está na linha {i} coluna {j}')
            v+=1
            break
    if v == 1:
        break    
else:
    print('Não está na matriz')        
       





