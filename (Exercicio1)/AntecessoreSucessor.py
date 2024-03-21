# #Antecessor e Sucessor de um número
#
# #Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.


numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print("O antecessor de", numero, "é", antecessor)
print("O sucessor de", numero, "é", sucessor)

# Lê os quatro números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

# Calcula a média
media = (numero1 + numero2 + numero3 + numero4) / 4

# Exibe o resultado
print("A média dos quatro números é:", media)