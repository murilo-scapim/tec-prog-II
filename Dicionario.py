diciplinas = {
    "TPII": "Técnicas de Programação II",
    "AOC": "Arquitetura e Organização de Computadores"
}

print(type(diciplinas))
print(diciplinas["TPII"])

diciplinas["ESI"] = "Engenharia de Software I"
# print(diciplinas["IA"]) chave não existe

print(diciplinas)

print("AOC" in diciplinas)
print("AOC" not in diciplinas)

for chave in diciplinas:
    print(diciplinas[chave])

for valor in diciplinas.values():
    print(valor)

for chave, valor in diciplinas.items():
    print(f"Chave: {chave}, Valor: {valor}")


estoque = {"banana": 50, "laranja": 12, "melancia": 17,
           "kiwi": 23}

for produto, quantidade in estoque.items():
    print(f"Temos {quantidade} unidades de {produto} no estoque")
