name = input("Digite o nome do jogo \n")
yearLaunch = int(input("Digite o ano de lançamento \n"))
gamePrice = float(input("Digite o preço do game\n"))
planIncluded = bool(input("Está incluso no plano!\n"))

print("###Dados do Game###")
print("===================")

#Forma Alternativa 1

# print("Nome do Jogo:", name)
# print("Ano de Lançamento:", yearLaunch)
# print("Preço do game:", gamePrice)
# print("Está incluso no plano?:", planIncluded)

#Forma Alternativa 2

# print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
#        "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

#Forma Alternativa 3

print(f"Nome do Jogo:{name} \nYear do Game:{yearLaunch} \nGame Price:{gamePrice} \nPlano Included: {planIncluded}")