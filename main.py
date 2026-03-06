from modulo import *
   
while True:
    """ Exibe o menu """
    print('----MENU----')
    print('digite o numero para iniciar "acao" ')
    print('1 -> adicionar: ')
    print('2 -> remove membro: ')
    print('3 -> listar equipe: ')
    print('0 -> sair: ')
    opcao= input('escolha uma opcao ')
    match opcao:
        case "1":
            adicionar_funcionario()
        case "2":
            remover_funcionario()
        case "3":
            listar_equipe()
        case "0":
            print('finalizando')
            exit()    
        case _:
            print(' o pecao invalida')
