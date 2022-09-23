num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

fazer = input("o que deseja fazer? \n a. + somar \n b. - diminuir  \n c. * multiplicar \n d. / dividir ")

soma = num1+num2
div = num1/num2
dim = num1-num2
multi =num1*num2

if fazer == "+":
    print(soma)
elif fazer == "-":
    print(dim)
elif fazer == "*":
    print(multi)
elif fazer == "/":
    print(div)