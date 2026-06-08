import json
estoque = {}

def carregarEstoque():
    try:
        with open ("estoque.json","r") as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return{}


def salvarEstoque():
    with open ("estoque.json","w") as arquivo:
        json.dump(estoque,arquivo)

def novoProduto():
    nome = input("Qual o nome do produto? ")
    if nome in estoque:
        print("esse produto já está no estoque")
        return
       
    quantidade = int(input("quantos vc deseja adicionar "))
    estoque[nome] = quantidade
    salvarEstoque()
    print("produto adicionado com sucesso")

def entProduto():
    nome = input("qual o nome do produto? ")
    if nome not in estoque:
        print("o produto não foi encontrado ")
        return
    quantidade = int(input("quantos itens vc deseja adicionar "))
    estoque[nome] += quantidade
    print("estoque foi atualizado")
    salvarEstoque()

def saidaProduto():
    nome =  input("qual o nome do produto? ")
    if nome not in estoque:
        print("o produto não foi encontrado")
        return
    
    quantidade = int(input("quantos itens vc deseja remover? "))
    if  quantidade > estoque[nome]:
        print("valor menor que o estoque atual")
        return
    estoque[nome] -= quantidade
    salvarEstoque()
    print("saída registrada")

def removerEstoque():
    nome = input("qual produto deseja remover? ")
    if nome not in estoque:
        print("o produto não foi encontrado")
        return
    
  
    del estoque[nome] 
    salvarEstoque()
    print("item foi removido")


def listaEstoque():
    print("\n===ESTOQUE===")

    if not estoque:
        print("o produto não foi encontrado")
        return
    
    for produto,quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

def menu():

    print("\n1 - novo produto")
    print("2 - Entrada de estoque")
    print("3 - Saída de estoque")
    print("4 - remover estoque")
    print("5 - Listar estoque")
    print("6 - Sair")

estoque = carregarEstoque()
while True:
    menu()

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        novoProduto()

    elif opcao == "2":
        entProduto()

    elif opcao == "3":
        saidaProduto()

    elif opcao == "4":
        removerEstoque()

    elif opcao == "5":
        listaEstoque()    

    elif opcao == "6":
        print("saindo...")
        break
    
    else:
        print("escolha uma opção valida")
        
                  



    



    



