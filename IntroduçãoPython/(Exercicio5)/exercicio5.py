def conta_letras(texto):
    maiusculas = 0
    minusculas = 0

    for caractere in texto:
        if caractere.isupper():
            maiusculas += 1
        elif caractere.islower():
            minusculas +=1
    return maiusculas, minusculas

texto_exemplo = "Hello World!"

num_maisculas, num_minusculas = conta_letras(texto_exemplo)
print("Numero de letras maiusculas:", num_maisculas)
print("Numero de letras minusculas:", num_minusculas)



def par_impar(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Corrigido para passar a lista corretamente
pares, impares = par_impar(lista)
print("Números pares da lista:", pares)
print("Números ímpares da lista:", impares)
