"""
Escreva uma função que calcule o fatorial de um número inteiro
não-negativo.
"""


def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)


num = int(input("Digite um numero inteiro para calcular seu fatorial: "))
resultado = fatorial(num)
print(f"O fatorial de {num} e igual a {resultado}")
