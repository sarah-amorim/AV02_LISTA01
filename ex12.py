"""
Crie uma função que converta uma temperatura de Celsius para Fahrenheit e
vice-versa.
"""


def cel_para_fah(celsius):
    return celsius * 1.8 + 32


def fah_para_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9


c = float(input("Digite a temperatura em Celsius para transformar em Fahrenheit: "))
resultado_fah = cel_para_fah(c)
print(f"{c}°C → {resultado_fah}°F")

fah = float(input("Digite a temperatura em Fahrenheit para transformar em Celsius: "))
resultado_c = fah_para_cel(fah)
print(f"{fah}°F → {resultado_c}°C")
