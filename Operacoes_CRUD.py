estoque = []

def buscar_produto(descricao):
    for produto in estoque:
        if produto["descricao"] == descricao:
            return produto
        else:
            return None


def exibir_menu():
    print("Escolha uma opção")
    print("1 - Mostrar estoque")
    print("2 - Adicionar produto")
    print("3 - Atualizar produto")
    print("4 - Remover produto")
    print("5 - Dar entrada no estoque")
    print("0 - Sair")

def exibir_estoque():
    if estoque:
        print("---- Estoque atual ---- ")
        for produto in estoque:
            print(f"Descrição: {produto['descricao']}"
                  f"| Preço unitário R$ {produto['preco_unitario']:.2f}"
                  f"| Quantidade {produto['quantidade']}")
    else:
        print("O estoque está vazio!")

def adicionar_produto():
    descricao = input("Digite a descrição do produto: ").strip().capitalize()

    if buscar_produto(descricao):
        print("Produto já existe no estoque!")
    else:
        preco_unitario = float(input("Digite o preço unitário: "))
        quantidade = int(input("Digite a quantidade: "))
        produto = {"descricao": descricao,
                   "preco_unitario": preco_unitario,
                   "quantidade": quantidade}
        estoque.append(produto)
        print("Produto adicionado com sucesso!")
