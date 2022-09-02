a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if (a.isdigit()):
    soma = a + b
    sub = a - b
    multi = a * b
    div = a/b
    resto = a%b

print('A soma é ', soma)
print('A subtração é ', sub)
print('A multiplicação é ', multi)
print('A divisão é ', div)
print('O resto da divisão é ', resto)
