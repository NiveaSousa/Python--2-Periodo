import random

def m(linha,coluna):

    matriz = []
    for i in range(linha):
        l = []
        for j in range(coluna):#Se quiser definir o conteudo
            l += [random.randint(0,50)]
        matriz += [l]

    return(matriz)


linha = int(input("Digite linhas: "))
coluna = int(input('Digite colunas: '))
print(m(linha, coluna))