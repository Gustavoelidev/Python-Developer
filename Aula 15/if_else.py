name = input("Digite o nome do game\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo"))
classification = float(input("Digite a nota de classificação do jogo"))

if classification > 8.0 or yearLaunch > 2015:
    print(f"o jogo {name} é incrivelmente bom!")
else:
    print(f"o jogo {name} ainda não atingiu uma boa nota. Por isso não recomendamos")