
def criarUsuario(auth):
    #Criando um usuário
    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    status = auth.create_user_with_email_and_password(user,password)
    print("Resultado: ", status)

