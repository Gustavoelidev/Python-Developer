### Cálculo da Distância

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,35 para viagens mais longas.

# distancia_km = float(input("Digite a distancia que voce deseja percorrer em km?\n"))
#
# if distancia_km <= 200:
#     preco_passagem = distancia_km * 0.50
# else:
#     preco_passagem = distancia_km * 0.35
#
# print("O preço da sua passagem sera de R$", preco_passagem)

## Aumento salário funcionário

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
# 15%.

salario_atual = float(input("Digite o valor do seu salario:\n"))

if salario_atual > 1250.00:
    aumento = salario_atual * 0.10
else:
    aumento = salario_atual * 0.15

novo_salario = salario_atual + aumento


print("O valor do aumento é R$", aumento)
print("O seu novo salario será de R$", novo_salario)