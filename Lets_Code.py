"""v0= float(input("Digite velocidade inicial em m/s: "))
y0 = float(input("Digite a posição inicial em metros: "))
t= float(input("Digite instante de tempo em segundos: "))
g = -10

yt = y0 + v0*t + (g*(t**2)/2)

print(yt)"""

#.isdigit()
#.replace(',','.', 1) Unica vez

idade = int(input("Digite sua idade: "))

if idade < 18:
	print("Menor de 18")
elif idade > 18:
	print("Maior de 18")