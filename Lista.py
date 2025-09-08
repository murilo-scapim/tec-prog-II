pessoas = ["Sofia", "Letícia", "Bruno", "Pedro"]

print(type(pessoas))  # type mostra o tipo de dados da variável
print(f"Tamanho: {len(pessoas)}")
print(pessoas[0])
# print(pessoas[4]) erro de índice
pessoas[1] = "Vinícius"

for pessoa in pessoas:
    print(pessoa)

for i in range(4):
    print(pessoas[0])

print(f"Min: {min(pessoas)}")
print(f"Max: {max(pessoas)}")

pessoas.append("Lucas")
print(pessoas)

print(f"Elemento removido: {pessoas.pop()}")
print(f"Elemento removido: {pessoas.pop(0)}")
print(pessoas)

pessoas.sort(reverse=True)
print(pessoas)

pessoas.reverse()
print(pessoas)

print(f"Índice: {pessoas.index('Pedro')}")

pessoas.remove("Bruno")
print(pessoas)
