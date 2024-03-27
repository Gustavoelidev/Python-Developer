""""
Exercício 4 

"""""
import random

done = False

while not done:
    print("O que voce deseja fazer?")
    print("1. Adivinhar o numero")
    print("2. Sair")

    choice = input(">")

    if choice == "1":
        print("====== ########################### =====")
        print("====== Adivinhe o numero de 1 a 10 =====")
        print("====== ########################### =====")
        number = int(input("Digite um numero de 1 a 10:\n "))
        result = random.randint(1, 10)
        if number == result:
            print("Parabens voce acertou!")
        else:
            print(f"Tente novamente, voce errou o numero sorteado foi {result} !")
    elif choice == "2":
        done = True
    else:
        print("Opcao invalida, escolha alguma das opcoes anteriores")