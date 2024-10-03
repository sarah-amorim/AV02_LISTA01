"""
Escreva uma função que calcule o fatorial de um número inteiro
não-negativo.
"""


def fatorial(numero):
    if numero == 0:
        return 1
    elif numero < 0:
        print("Digite um numero inteiro nao-negativo")
    else:
        return numero * fatorial(numero - 1)


while True:
    try:
        num = int(input("Digite um numero inteiro para calcular seu fatorial: "))
        resultado = fatorial(num)
        print(f"O fatorial de {num} e igual a {resultado}")
    except ValueError:
        print("Digite um numero valido")
