import time
import winsound  # Para Windows

# Faz a contagem regressiva de 10 até 0
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Espera por 1 segundo antes de imprimir o próximo número

# Emite um som de beep ao final da contagem regressiva
winsound.Beep(1000, 1000)  # Frequência de 1000 Hz por 1 segundo (1000 ms)

numero = int(input("Digite um número para o qual  deseja ser calculo pela tabuada:\n"))

inicio = int(input("Digite o valor inicial:\n"))

fim = int(input("Digite o valor final da tabuada:\n"))

print(f"Tabuada do {numero} de {inicio} até {fim}:\n")

for i in range(inicio, fim +1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")