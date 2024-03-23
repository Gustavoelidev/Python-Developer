gameslist = ["Fifa 24","GTA VI", "Star Wars",
             "The Legend of Zelda", "Barbie","Barbie2"]

# 1 - Tamanho da lista
print(len(gameslist))

# 2 - Recuperar um item da listra pelo indice

print(gameslist.index("Barbie"))

# 3 - Adicionar um item ao final da lista

print(gameslist.append("BF2024"))
print(gameslist)

# 4 - Ordenar a lista

gameslist.sort()
print(gameslist)

# 5 - copiar os itens de uma lista para outra

gameReset = gameslist.copy()
gameReset.remove("Star Wars")
print(gameReset)

# 6 - Remove todos os itens da lista

gameslist.clear()
print(gameslist)

