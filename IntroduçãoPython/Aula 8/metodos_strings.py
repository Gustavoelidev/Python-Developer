gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo, de mundo, aberto
desenvolvido pela EA Sports.
"""

print(gameName.upper()) #retornar string em maiuscula
print(gameName.lower()) #retornar string em minuscula
print(gameName.capitalize()) #Apenas a primeira letra maiuscula
print(gameName.title()) #Apenas a primeira letra em maiuscula
print(gameName.center(11,'-')) #centraliza
print(gameName.find('a')) #retorna posicção de um caracter.
print(gameDescription.count("a")) #conta caracteres
print(gameDescription.count("f")) #conta caracteres
print(gameDescription.replace("Fifa","Pes")) #altera elementos
print(gameDescription.split(','))
