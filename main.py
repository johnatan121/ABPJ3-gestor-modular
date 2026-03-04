equipe = {}

def adicionar_funcionario():
    no=input(print('digite o nome do funcionario'))
    de=input(print('digite o departamento'))
    equipe[no]=de

def remover_funcionario():
    if no in equipe:
        remove.pop(equipe)

def menu():
    print('digite o numero para acao ')
    print('1 -> adicionar:')
    print('2 -> remove membro:')
    print('0 -> sair:')
    opcao= input('digite uma opcao ')
    match opcao:
        case "1":
            adicionar_funcionario()
        case "2":
            remover_funcionario()
        case "0":
            print('finalizando')
            exit()    
        case _:
            print(' o pecao invalida')

print(equipe)
while True:
    menu()
