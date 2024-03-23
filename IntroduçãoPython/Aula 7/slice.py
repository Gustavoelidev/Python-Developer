gameName = "GTA VI"
gameDescription = """
GTA VI é um jogo de mundo aberto
desenvolvido pela Rockstar.
"""

# string[inicio:fim] - indice começa na posição 0 | indice final -1

# 1 - Busque toda string a partir da primeira posição

print(gameName[0:])

# 2 - Busque toda string ate a ultima posição
print(gameName[:5])

# 3 - Busque toda string da terceira ate a ultima posição

print(gameName[2:])

"""
 string[inicio:fim] - indice começa na posição 0 | indice final -1 passo - determina o incremento. Por padrão esse número é o 1.
"""
# 4 - Busque toda string de 2 em 2 caracteres

print(gameName[::2])

# 5 - Busque toda string nos indices impares

print(gameName[1::2])

# 6 - Inverter uma string de tras pra frente

print(gameName[::-1])
