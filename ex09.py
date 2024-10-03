"""
Crie uma função que receba uma lista de números e retorne a soma de todos
os elementos da lista.
"""


def soma(lista_de_numeros):
    resultado = sum(lista_de_numeros)
    print(f"A soma desses valores e igual a {resultado}")


while True:
    try:
        qnt = int(input("Quantos numeros deseja somar? "))

        numeros = []

        for i in range(qnt):
            numero = int(input("Numero: "))
            numeros.append(numero)

        soma(numeros)

    except ValueError:
        print("Digite numeros validos")
