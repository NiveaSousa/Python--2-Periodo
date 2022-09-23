import random

matriz = []
c = []
for i in range(5):
    linha = []
    for j in range(5):
        num = random.randint(0,9)
        linha += [num]
        if not c.__contains__(num):
            c.append(num)
    matriz += [linha]

x = 0
y = 0


for i in range(5):
    for j in range(5):
        if x < matriz[i][j]:
            y = x
            x = matriz[i][j]
            
            

c.sort()
y = c[len(c)-2]

for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])

print(f'Segundo maior número é: {y} - {x}')