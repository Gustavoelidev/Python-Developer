# Função para adicionar um time
def adicionar_time(times):
    nome_time = input("Digite o nome do seu time:\n")
    times.append({"nome": nome_time, "jogadores": []})  # Usando 'jogadores' em minúsculo
    print("Time adicionado com sucesso!\n")


# Função para listar times
def listar_times(times):
    print("Times cadastrados:")
    for indice, time in enumerate(times):
        print(f"{indice}: {time['nome']} - {len(time['jogadores'])} jogadores")


# Função para adicionar jogador em um time
def adicionar_jogador(times):
    print("Times cadastrados:\n")
    for indice, time in enumerate(times):
        print(f"{indice}: {time['nome']} - {len(time['jogadores'])} jogadores")
    indice_time = int(input("Digite o índice do time que deseja adicionar o jogador:\n "))
    if 0 <= indice_time < len(times):
        nome_jogador = input("Digite o nome do jogador:\n")
        times[indice_time]['jogadores'].append(nome_jogador)
        print("Jogador adicionado com sucesso!")
    else:
        print("Índice inválido.")


# Função para remover jogador de um time
def remover_jogador(times):
    print("Times cadastrados:\n")
    for indice, time in enumerate(times):
        print(f"{indice}: {time['nome']} - {len(time['jogadores'])} jogadores")
    indice_time = int(input("Digite o índice do time que deseja remover o jogador:\n"))
    if 0 <= indice_time < len(times):
        print("Jogadores cadastrados:")
        for indice, jogador in enumerate(times[indice_time]['jogadores']):
            print(f"{indice}: {jogador}")
        indice_jogador = int(input("Digite o índice do jogador que deseja remover: "))
        if 0 <= indice_jogador < len(times[indice_time]['jogadores']):  # Corrigindo a verificação de índice
            del times[indice_time]['jogadores'][indice_jogador]  # Removendo o jogador corretamente
            print("Jogador removido com sucesso!")
        else:
            print("Índice inválido.")
    else:
        print("Índice de time inválido.")


# Função para listar jogadores de um time
def listar_jogadores(times):
    print("Times cadastrados:\n")
    for indice, time in enumerate(times):
        print(f"{indice}: {time['nome']} - {len(time['jogadores'])} jogadores")
    indice_time = int(input("Digite o índice do time que deseja listar os jogadores:\n"))
    if 0 <= indice_time < len(times):
        print(f"Jogadores do time {times[indice_time]['nome']}:")
        for jogador in times[indice_time]['jogadores']:  # Corrigindo o uso de variáveis
            print(jogador)
    else:
        print("Índice inválido!")


# Função principal
def main():
    times = []
    while True:
        print("\n--- Menu ---")
        print("1 - Adicionar um time")
        print("2 - Listar times")
        print("3 - Adicionar jogador em um time")
        print("4 - Remover jogador de um time")
        print("5 - Listar jogadores de um time")
        print("0 - Sair do programa")
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            adicionar_time(times)
        elif opcao == "2":
            listar_times(times)
        elif opcao == "3":
            adicionar_jogador(times)
        elif opcao == "4":
            remover_jogador(times)
        elif opcao == "5":
            listar_jogadores(times)
        elif opcao == "0":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
