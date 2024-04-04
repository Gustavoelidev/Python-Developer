class Viagem:
    def __init__(self, destino):
        self.destino = destino


destinos_disponiveis = ['Paris', 'Londres', 'Portugal', 'Sydney', 'Brazil']

def cadastrar_viagem():
    nome_usuario = input("Digite seu nome:")
    destino_viagem = input("Escolha o destino (Paris, Londres, Portugal, Sydney:)\n")

    if destino_viagem.capitalize() in destinos_disponiveis:
        viagem = Viagem(destino_viagem.capitalize())
        print(f"O cadastro da viagem para {viagem.destino} foi feita com sucesso para {nome_usuario}!")
    else:
        print(f"Destino invalido, por favor digite outro destino valido")

cadastrar_viagem()