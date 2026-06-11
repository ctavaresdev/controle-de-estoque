import sqlite3

def criarTabela():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE,
        quantidade INTEGER
                   
) 
""")

    conexao.commit()

    conexao.close()


def novoProduto():
    nome = input("Qual o nome do produto? ")
    quantidade = int(input("quantos vc deseja adicionar "))

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO produtos(nome, quantidade)
            VALUES (?, ?)
            """,
            (nome,quantidade)
        )

        conexao.commit()
        print("estoque atualizado com sucesso!")

    except sqlite3.IntegrityError:
        print("o produto já existe!")

    finally:
        conexao.close()

def entProduto():
    nome = input("qual o nome do produto? ")
    quantidade = int(input("quantos itens vc deseja adicionar? "))

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT quantidade FROM produtos WHERE nome = ?",
        (nome,)

    )

    resultado = cursor.fetchone()

    if resultado is None:
        print("Produto não encontrado!")
        conexao.close()
        return
    
    quantidade_atual = resultado[0]

    nova_quantidade = quantidade_atual + quantidade

    cursor.execute(
    """
        UPDATE produtos
        SET quantidade = ?
        WHERE nome = ?
        """,
        (nova_quantidade, nome)
    )

    conexao.commit()
    conexao.close()

    print("Estoque atualizado!")


def saidaProduto():
    nome =  input("qual o nome do produto? ") 
    quantidade = int(input("quantos itens vc deseja remover? "))

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT quantidade FROM produtos WHERE nome = ?",
        (nome,)

    )

    resultado = cursor.fetchone()

    if resultado is None:
        print("Produto não encontrado!")
        conexao.close()
        return
    
    quantidade_atual = resultado[0]

    if quantidade > quantidade_atual:
        print("quantidade insuficiente no estoque!")
        conexao.close()
        return
    
    nova_quantidade = quantidade_atual - quantidade

    cursor.execute(
    """
        UPDATE produtos
        SET quantidade = ?
        WHERE nome = ?
        """,
        (nova_quantidade, nome)
    )

    conexao.commit()
    conexao.close()

    print("Estoque atualizado!")

def removerProduto():
    nome = input("Nome do produto: ")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute(
    "SELECT * FROM produtos WHERE nome = ?",
    (nome,)
    )

    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado!")
        conexao.close()
        return

    cursor.execute(
    "DELETE FROM produtos WHERE nome = ?",
    (nome,)
    )

    conexao.commit()
    conexao.close()

    print("Produto removido com sucesso!")


def listaEstoque():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    conexao.close()

    print("\n=== ESTOQUE ===")

    for id_produto, nome, quantidade in produtos:
        print(f"ID: {id_produto}")
        print(f"Nome: {nome}")
        print(f"Quantidade: {quantidade}")
        print("-" * 20)
    

def menu():

    print("\n1 - novo produto")
    print("2 - Entrada de estoque")
    print("3 - Saída de estoque")
    print("4 - remover estoque")
    print("5 - Listar estoque")
    print("6 - Sair")

criarTabela()
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
        removerProduto()

    elif opcao == "5":
        listaEstoque()    

    elif opcao == "6":
        print("saindo...")
        break
    
    else:
        print("escolha uma opção valida")
        
                  



    



    



