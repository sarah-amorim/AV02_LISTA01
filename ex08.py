"""
Escreva uma função que receba um número e retorne True se ele for primo e
False caso contrário.
"""


def primo(numero):
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    if divisores[0] == 1 and divisores[1] == numero:
        return True
    else:
        return False


while True:
    try:
        num = int(input("Digite um numero para saber se ele e primo (True) ou nao (False): "))

        if num < 0:
            print("Digite um numero positivo")
            break

        resultado = primo(num)
        print(resultado)

    except ValueError:
        print("Digite um numero valido")
