num1 = float(input("Digite o numero1:\n "))
num2 = float(input("Digite o numero2:\n "))

operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação invalida")
    result = 0

print(f"O resultado é igual a {result:.2f}")
