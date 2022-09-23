matriz = []
x = 0

for i in range(2):
    linha = []
    for j in range(2):
        if j == i:
            x = 1
        else:
            x = 0
        linha += [x]
    matriz += [linha]
    


print(matriz)

        