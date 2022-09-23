import random

matriz = []
resp = ['a','b','c','d','a']
x = []

for i in range(3):
    linha = []
    for j in range(5):
        linha += [random.choice('abcd')] #random de letras
    matriz += [linha]

for i in range(3): # imprimir um abaixo do outro
    print(matriz[i])
    
    

for i in range(3):
    for j in range(5):
        x.append(matriz[i][j])
        if x == resp[j]:
            print(f'O resultado está correto')
        else:
            print(f'Resultado incorreto. Resposta é {resp[j]}')