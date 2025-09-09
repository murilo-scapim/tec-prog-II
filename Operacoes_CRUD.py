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

def atualizar_produto():
    if estoque:
        descricao = input("Digite a descrição do produto: ")

        produto_encontrado = buscar_produto(descricao)

        if produto_encontrado:
            nova_descricao = input("Digite a nova descrição: ")
            novo_preco_unitario = float(input("Digite o novo preço unitário: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))

            produto_encontrado["descricao"] = nova_descricao
            produto_encontrado["preco_unitario"] = novo_preco_unitario
            produto_encontrado["quantidade"] = nova_quantidade

            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado!")
    else:
        print("Estoque está vazio!")

def apagar_produto():
    if estoque:
        descricao = input("Digite a descrição do produto: ")
        produto_encontrado = buscar_produto(descricao)

        if produto_encontrado:
            estoque.remove(produto_encontrado)
            print("Produto apagado com sucesso!")
        else:
            print("Produto não existe!")
    else:
        print("O estoque está vazio!")

# Implementar a função para realizar entrada de estoque