gamesTuple = ["Fifa 24", "GTA VI", "Star Wars",
              "The Legend of Zelda", "Barbie"]

print(gamesTuple)
print(type(gamesTuple))
# name = ("Rodrigo",)
# print(type(name))

# 1 - Buscar os dois primeiros itens da tupla

print(gamesTuple[:2])

# 2 - Buscar o ultimo iten da tupla

print(gamesTuple[:-1])

# 3 - Buscar ate uma determinada posição

print(gamesTuple[:3])

# 4 - Buscar ate uma  posição em diante

print(gamesTuple[2:])

# 5 - recuperar um item da tupla pelo indice

print(gamesTuple.index('Star Wars'))



# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla
