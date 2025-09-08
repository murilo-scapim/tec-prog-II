estoque = []

while True:
    escolha = input("Escolha uma opção:\n"
                    "1 - Mostrar estoque\n"
                    "2 - Adicionar produto\n"
                    "3 - Atualizar produto\n"
                    "4 - Remover produto\n"
                    "5 - Dar entrada no estoque\n"
                    "0 - Sair ")

    if escolha == "1":
        if estoque:
            print("Estoque atual:")
            for produto in estoque:
                print(f"Descrição: {produto['descricao']}"
                      f"Preço unitário: R${produto['valor_unitario']}"
                      f"Quantidade: {produto['quantidade']}")
        else:
            print("O estoque está vazio!")
    elif escolha == "2":
        descricao = input("Digite a descrição: ")

        produto_existente = False
        for produto in estoque:
            if produto["descricao"] == descricao:
                produto_existente = True
                break

        if produto_existente:
            print("Produto já existe no estoque!")
        else:
            valor_unitario = float(input("Digite o valor unitário: "))
            quantidade = int(input("Digite a quantidade: "))
            produto = {"descricao": descricao, "valor_unitario": valor_unitario,
                       "quantidade": quantidade}
            estoque.append(produto)
            print("Produto inserido com sucesso!")
    elif escolha == "3":
        if estoque:
            descricao = input("Digite a descrição do produto a ser atualizado: ")

            produto_encontrado = None
            for produto in estoque:
                if produto["descricao"] == descricao:
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não existe no estoque!")
            else:
                nova_descricao = input("Digite a nova descrição: ")
                novo_valor_unitario = float(input("Digite o novo valor unitário: "))
                nova_quantidade = int(input("Digite a nova quantidade: "))

                produto_encontrado["descricao"] = nova_descricao
                produto_encontrado["valor_unitario"] = novo_valor_unitario
                produto_encontrado["quantidade"] = nova_quantidade
                print("Produto atualizado com sucesso!")
        else:
            print("O estoque está vazio!")
    elif escolha == "4":
        if estoque:
            descricao = input("Digite o nome do produto para remover: ")

            produto_encontrado = None
            for produto in estoque:
                if produto["descricao"] == descricao:
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não existe no estoque!")
            else:
                estoque.remove(produto_encontrado)
                print("Produto removido com sucesso!")
        else:
            print("O estoque está vazio!")
    elif escolha == "5":
        if estoque:
            descricao = input("Digite o nome do produto para remover: ")

            produto_encontrado = None
            for produto in estoque:
                if produto["descricao"] == descricao:
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não existe no estoque!")
            else:
                quantidade = int(input("Digite a quantidade: "))
                produto_encontrado["quantidade"] += quantidade
                print("Entrada de estoque realizada com sucesso!")
        else:
            print("O estoque está vazio!")
    elif escolha == "0":
        print("Programa encerrado!")
        break
    else:
        print("Opcão inválida! Tente novamente...")
