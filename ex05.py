from autenticar.controlador_usuario import autenticar

login = input("Login: ")
senha = input("Senha: ")

autenticar(username=login, password=senha)
