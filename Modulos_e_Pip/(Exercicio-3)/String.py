""""
Exercício 3 

Verificar conteúdo da String

Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
"""""
import re

def verificar(string):
    padrao = re.compile(r'^[a-zA-Z0-9]+$')
    if padrao.match(string):
        return True
    else:
        return False

string = "AbC123"
string2 = "abc@123"

print(verificar(string))
print(verificar(string2))