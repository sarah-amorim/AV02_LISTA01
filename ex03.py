"""
Crie uma calculadora utilizando funções
a. Obrigatoriamente você deve ter funções: somar, subtrair, multiplicar e dividir
    i. Todas recebem 2 números como parâmetro de entrada
"""


def calculadora(num01, num02):
    soma = num01 + num02
    sub = num01 - num02
    mult = num01 * num02
    div = num01 / num02
    
    print("\n")
    print(f"SOMA: {soma}")
    print(f"SUBTRAÇAO: {sub}")
    print(f"MULTIPLICAÇAO: {mult}")
    print(f"DIVISAO: {div}")


print("CALCULADORA")
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
calculadora(n1, n2)
