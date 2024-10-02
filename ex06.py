"""
Crie uma função que receba uma string e retorne o número de vogais
presentes na string.
"""


def vogais(string):
    quantidade = 0
    for letras in string:
        if "a" in letras:
            quantidade += 1
        if "e" in letras:
            quantidade += 1
        if "i" in letras:
            quantidade += 1
        if "o" in letras:
            quantidade += 1
        if "u" in letras:
            quantidade += 1

    return quantidade


palavra = input("Digite algo para saber o numero de vogais presentes na string: ")
resultado = vogais(palavra)
print(f"A qauntidade de vogais em '{palavra}' e igual a {resultado}")
