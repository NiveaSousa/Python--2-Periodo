import random

matriz = []
x = []

for i in range(6):
    linha = []
    for j in range(6):
        linha += [random.randint(1,100)]
       
    matriz += [linha]


for i in range(6):
    for j in range(6):
        if j == i:
            x.append(matriz[i][j])

print(matriz)

print(x)