estoque = {}

def adcProduto():
    nome = input("Qual o nome do produto? ")
    if nome in estoque:
        print("esse produto já está no estoque")
        return
       
    quantidade = int(input("quantos vc deseja adicionar "))
    estoque[nome] = quantidade
    print("produto adicionado com sucesso")

def entProduto():
    nome = input("qual o nome do produto? ")
    if nome not in estoque:
        print("o produto não foi encontrado ")
        return
    quantidade = int(input("quantos itens vc deseja adicionar "))
    estoque[nome] += quantidade
    print("estoque foi atualizado")

def saidaProduto():
    nome =  input("qual o nome do produto?")
    if nome not in estoque:
        print("o produto não foi encontrado")
        return
    
    quantidade = int(input("quantos itens vc deseja remover?"))
    if  quantidade > estoque[nome]:
        print("valor menor que o estoque atual")
        return
    estoque[nome] -= quantidade
    print("saída registrada")

def listaEstoque():
    print("\n===ESTOQUE===")

    if not estoque:
        print("o produto não foi encontrado")
        return
    
    for produto,quantidade in estoque.items():
        print(f"{produto}:{quantidade}")

def menu():

    print("\n1 - Adicionar produto")
    print("2 - Entrada de estoque")
    print("3 - Saída de estoque")
    print("4 - Listar estoque")
    print("5 - Sair")

while True:
    menu()

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        adcProduto()

    elif opcao == "2":
        entProduto()

    elif opcao == "3":
        saidaProduto()

    elif opcao == "4":
        listaEstoque()

    elif opcao == "5":
        print("saindo...")
        break
    
    else:
        print("escolha uma opção valida")
        
                  



    



    



