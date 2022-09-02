import random

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        linha += [random.randint(10,50)]
    matriz += [linha]

x = 0

for i in range(10):
    for j in range(10):
        if not j == i:
            if x < matriz[i][j]:
                x = matriz[i][j]
    

for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])


print(f'Maior número é: {x}')