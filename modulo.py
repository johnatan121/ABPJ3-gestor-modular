
equipe = {}

def adicionar_funcionario():
    """entra com os dados do funcionaro"""
    nome =input('digite o nome do funcionario ')
    departamento=input('digite o departamento ')
    print(' cadastro realizado ')
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
        for nome, departamento in equipe.items():
            print(f"{nome} - {departamento} ")
   
