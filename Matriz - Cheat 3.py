matriz = []
x = 0

for i in range(5):
    linha = []
    for j in range(5):
        x = int(i * j)
        linha += [x]
    matriz += [linha]
    

for i in range(i): # imprimir um abaixo do outro
    print(matriz[i])
