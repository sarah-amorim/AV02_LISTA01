"""
a. Feita a questão 3 crie uma função calcular que recebe 3 parâmetros:
    i. numero1, numero2 e operação (pode ser somar; subtrair; multiplicar e dividir)
"""


def calculadora(opcao, numero01, numero02):
    if opcao == 1:
        soma = numero01 + numero02
        print(f"{numero01} + {numero02} = {soma}")
    elif opcao == 2:
        subtracao = numero01 - numero02
        print(f"{numero01} - {numero02} = {subtracao}")
    elif opcao == 3:
        mult = numero01 * numero02
        print(f"{numero01} * {numero02} = {mult}")
    elif opcao == 4:
        div = numero01 / numero02
        print(f"{numero01} / {numero02} = {div:.2}")
    else:
        print("Digite uma opcao valida")


print("CALCULADORA")
while True:
    try:
        print("\nSOMA [1]")
        print("SUBTRAÇAO [2]")
        print("MULTIPLICAÇAO [3]")
        print("DIVISAO [4]\n")

        opc = int(input("Digite o numero da operaçao deseja executar: "))

        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        calculadora(opc, n1, n2)

    except ZeroDivisionError and ValueError:
        print("\nDigite um numero valido")
