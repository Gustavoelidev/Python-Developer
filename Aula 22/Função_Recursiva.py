""""
Fatorial de um numero :

3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""""

# 1 - Fatorial de um numero

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num -1))

number = int(input('Digite um numero para fatorial\n'))
print(f"O fatorial de {number} é: {fatorial(number)}")

# 2 - soma total de um numero

""""
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
"""""

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num -1))

num = int(input('Digite um numero para soma:\n'))
print(f"A soma de {num} é: {total_sum(num)}")