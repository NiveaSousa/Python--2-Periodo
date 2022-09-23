fat = int(input('Digite um número: '))
resultado = 1

while (fat>=1):
	resultado *=fat
	#guardar o valor da multiplicação
	fat -= 1
print(f'Fatorial = {resultado}')