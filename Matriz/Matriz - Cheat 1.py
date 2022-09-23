matriz = []
x = 0

for i in range(2):
    linha = []
    for j in range(2):
        linha += [int(input())]
    matriz += [linha]

print(matriz)

for l in range(2):
    for i in range(2):
         if matriz[l][i] > 10:
            x+=1

print(x)
           
    