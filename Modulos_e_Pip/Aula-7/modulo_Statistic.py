import statistics

# 1 aplicar media

print(statistics.mean([1, 2, 3, 4, 5]))

# 2 aplicar a mediana

print(statistics.median([1, 2, 3, 4, 5]))
print(statistics.median([1, 2, 3, 4, 5, 8]))

# 3 aplicar a moda

print(statistics.mode([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 8, 2]))

# Aplicar o desvio padrão
"""
Medida de dispersão do conjunto, ou seja, uma medida 
que indica quão uniformes são os dados do conjunto.

- Quanto mais próximo de 0, significa que os dados
do conjunto estão menos dispersos
"""

print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))