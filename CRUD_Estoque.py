from Operacoes_CRUD import *

while True:
    exibir_menu()

    escolha = input("Digite a opção: ")

    if escolha == "1":
        exibir_estoque()
    elif escolha == "2":
        adicionar_produto()