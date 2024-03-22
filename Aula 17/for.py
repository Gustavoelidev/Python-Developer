gameList = ["GTA V", "FIFA 23", "RED DEAD 2", "LOL"]

# 1 - AIterando vcalores de uma lista
for game in gameList:
    print(game)

# 2 - quando a condição for atendida, o loop sera encerrado.

for game in gameList:
    if game == "RED DEAD 2":
        break
    print(game)

# 3 - Quando a condição for atendida o Loop vai para proxima interação

for game in gameList:
    if game == "RED DEAD 2":
        continue
    print(game)

# 4 - Avaliação do jogo

gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo \n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating}")
