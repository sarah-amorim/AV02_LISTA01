"""
Crie uma função que receba uma string e retorne o número de palavras na string
"""


def num_palavras(string):
    return len(string.split(" "))


palavras = input("Digite um texto para saber a quantidade de palavras: ")
resultado = num_palavras(palavras)
print(f"O numero de palavras e igual a {resultado}")
