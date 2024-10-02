"""
Crie uma função que receba um email e retorna se ele possui ‘@’
○ Desafio: Para aprimorar pesquise sobre regex e retorne se o e-mail é válido

Usei esse site para saber sobre regex: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
"""
import re


def validar_email(email):
    resultado = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

    if resultado:
        return f"Email valido"
    else:
        return f"Email invalido"


endereco_email = input("Email: ")
print(validar_email(endereco_email))
