matriz = []
n_linhas = int(input())
n_colunas = int(input())
for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):#Se quiser definir o conteudo
        linha += [input()]
    matriz += [linha]

print(matriz)

for l in range(n_linhas): # imprimir um abaixo do outro
    print(matriz[l])

for i in range(n_linhas): #Só para matriz quadradas
    print(matriz[0][i]) #Se eu quiser a linha
    print(matriz[i][0]) #Se eu quiser a coluna
