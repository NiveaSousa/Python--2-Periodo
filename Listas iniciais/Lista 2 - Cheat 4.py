mediag = 0

for i in range(15):
    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite sua nota: "))
    nota2 = float(input("Digite sua 2ª nota: "))
    media = (nota1+nota2)/2
    print(f'{nome} tirou {nota1} na primeira nota e {nota2} na segunda, ficando com a média {media}')
    mediag = mediag + media


print(f' A média geral da turma é {mediag/15}')
