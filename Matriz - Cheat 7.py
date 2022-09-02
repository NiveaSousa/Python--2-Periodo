import random

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha += [random.randint(0,99)]
    matriz += [linha]

x = 0
y = 0

for i in range(5):
    for j in range(5):
        if x < matriz[i][j]:
            y = x
            x = matriz[i][j]





for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])

print(f'Segundo maior número é: {y}')