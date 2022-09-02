manifestacoes = [ ]
opcao = '0'

while opcao != '4':
    print('''Sistema de Ouvidoria
        Menu do Sistema
        Opcoes:
        1 ABRIR CHAMADOS
        2 LISTAR CHAMADOS
        3 REMOVER
        4 SAIR''')
    opcao = input('Digite a sua opcao ')

    if opcao == '1':
        print('Agora vamos criar um novo chamado')
        titulo = input('Digite o problema ')
        manifestacoes.append(titulo)

    elif opcao == '2':
        print('Chamados: ')
        for item in manifestacoes:
            print(item)
        print('Fim')

    elif opcao == '3':
        remover = int(input('Qual Chamado você deseja remover?'))
        remover -= 1
        manifestacoes.pop(remover)


print('Obrigado por usar o Sistema de Ouvidoria da nossa empresa')