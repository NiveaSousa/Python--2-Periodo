import registros_classe


opcao = '0'
novo = registros_classe.Chamado()
while opcao != '4':

    print('Sistema de Ouvidoria\n Menu do Sistema\n Opcoes:\n 1 ABRIR CHAMADOS\n 2 LISTAR CHAMADOS\n 3 REMOVER\n 4 SAIR')
    opcao = input('Digite a sua opcao ')

    if opcao == '1':
        titulo = input('Digite o problema ')
        print(novo.cadastrar(titulo))

    elif opcao == '2':
        novo.listChamado()


    elif opcao == '3':
        novo.removeChamado()
        

print('Obrigado por usar o Sistema de Ouvidoria da nossa empresa')