import random

matriz = []
x = []

for i in range(10):
    linha = []
    for j in range(10):
        linha += [random.randint(10,50)]
    matriz += [linha]


for i in range(10):
    for j in range(10):
        if (j + i) == (10-1):
            x.append(matriz[i][j])

for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])


print(f'A diagonal secundária é: {x}')

somax= sum(x)

media = somax/len(x)

print(f'O valor da média é: {media}')



