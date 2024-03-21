import pprint

gameDict =  {
    "resident evil 4": {
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["acão", "aventura"]
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["3d", "aventura"]
    },
    "donkey kong country": {
            "yearLaunch": 1995,
            "classification": 9.5,
            "genre": ["plataforma", "aventura"]
        },
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gameDict)

# 1 -buscar informação dentro de um dicionario alinhado

print(gameDict["mario odyssey"]["genre"])

# 2 - adicionar um novo item

gameDict["mario odyssey"]["players"] = 1
print(gameDict["mario odyssey"])

# 3 - exluir um dicionario

del gameDict["resident evil 4"]
pp.pprint(gameDict)

