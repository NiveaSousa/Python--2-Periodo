import random

matriz1 = []
matriz2 = []


for i in range(2):
    linha = []
    for j in range(2):
        linha += [random.randint(1,2)]
    matriz1 += [linha]

for i in range(2):
    linha = []
    for j in range(2):
        linha += [random.randint(1,2)]
    matriz2 += [linha]

opcao = '0'

print('''Escolha a opção:
    1 Somar as duas matrizes
    2 Subtrair a primeira matriz da segunda
    3 Adicionar uma constante às duas matrizes
    4 Imprimir as matrizes''')
opcao = input('Digite a sua opcao ')
x = []
somaLinha = []
dimLinha = []
if opcao == '4':
    for i in range(2):
        print(matriz1[i])
        print(matriz2[i])



elif opcao == '1':
	print(matriz1)
	print(matriz2)
	for i in range(2): 	
		somaLinha.append([])
		for j in range(2):
			linha = matriz1[i][j] + matriz2[i][j]
			somaLinha[i].append(linha)
		
	print(f'{somaLinha} aqui')
			



elif opcao == '2':
    print(matriz1)
	print(matriz2)
	for i in range(2): 	
		dimLinha.append([])
		for j in range(2):
			linha = matriz1[i][j] - matriz2[i][j]
			dimLinha[i].append(linha)
		
	print(f'{dimLinha} aqui')


    
