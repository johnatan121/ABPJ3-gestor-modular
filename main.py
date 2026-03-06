equipe = {}

def adicionar_funcionario():
    """entra com os dados do funcionaro"""
    nome =input('digite o nome do funcionario ')
    departamento=input('digite o departamento ')
    equipe[nome]=departamento

def remover_funcionario():
    """ faz a remocao do funcionario"""
    nome=input('digite o nome do funcionario ')
    if nome in equipe:
        equipe.pop(nome)
        return equipe
    else:
        print('funcionario nao encontrado ')

def listar_equipe():
    """Exibe todos os funcionários cadastrados."""
    print("\n--- Equipe Atual ---")
    if not equipe:
        print("Equipe vazia.")
    else:
        for nome, departamento in equipe.items:
            print(f"{nome} - {departamento} ")
   
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
