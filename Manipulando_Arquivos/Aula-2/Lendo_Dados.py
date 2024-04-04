# r - leitura
# w - escrita
# a - append
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f" olá, {line.rstrip()}")
