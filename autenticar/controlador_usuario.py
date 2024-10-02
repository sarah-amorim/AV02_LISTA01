def autenticar(username, password):
    usuarios = [
        {
            "username": "teste",
            "password": "admin"
        },
        {
            "username": "teste2",
            "password": "admin2"
        },
        {
            "username": "teste3",
            "password": "admin3"
        },
        {
            "username": "teste4",
            "password": "admin4"
        }
    ]

    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print('Usuario encontrado')
            break
        else:
            print("Usuario nao encontrado")
            break
