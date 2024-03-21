gameFifa =  {
    "name": "Fifa 23",
    "yearLaunch": 2023,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte","familia"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# recuperar um elemento do dicionario

print(gameFifa['genre'])
print(gameFifa.get('classification'))

# recuperar apenas chaves do dicionario

print(gameFifa.keys())

# recuperar apenas chaves do dicionario

print(gameFifa.values())

# buscar itens do dicionario com cahve e valor

print(gameFifa.items())

# adicionar itens no dicionario

gameFifa["players"] = 2
print(gameFifa)

# atualizar itens do dicionario

gameFifa.update({"players": 1})
print(gameFifa)

# remover item do dicionario

gameFifa.pop("players")
print(gameFifa)