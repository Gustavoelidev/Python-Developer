"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo,
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

# Apresentação de cursos Kwargs

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

presentation(name = "python", category = "Backend", level = "iniciante")
presentation(name = "Redes em computadores", category = "Redes", level = "Iniciante")
presentation(name = "AQ", category = "Qualidade em produtos", level = "Iniciante")