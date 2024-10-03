"""
Crie uma função que receba uma lista de números e retorne a média.
"""


def media(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)


numeros = []
while True:
    try:
        quantidade = int(input("Digite quantos numeros deseja adicionar: "))
        if quantidade < 0:
            print("Digite um numero valido")
            break

        for i in range(quantidade):
            numero = float(input("Valor: "))
            numeros.append(numero)

        resultado = media(numeros)
        print(f"A media dos valores e igual a {resultado:.2}")

    except ValueError and ZeroDivisionError:
        print("Digite numeros validos")
