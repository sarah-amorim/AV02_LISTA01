"""
Faça um programa, com uma função que necessite de um parâmetro “número”. A função retorna o valor de
caractere ‘P’, se seu valor for positivo, e ‘N’, se seu valor for zero ou negativo
"""


def verificar(numero):

    if numero > 0:
        print("P")
    elif numero < 0:
        print("N")
    else:
        print("neutro")


while True:
    try:
        num = int(input("Digite um numero para saber se ele e positivo ou negativo: "))
        verificar(num)
    except ValueError:
        print("Valor invalido, digite um numero inteiro!")
