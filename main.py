import os
import stat
import pyrebase
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyA42zCegZDuOOJzyVMXqsUWmqVFGXUyqIE",
    "authDomain": "fir-pucpr-d6409.firebaseapp.com",
    "projectId": "fir-pucpr-d6409",
    "databaseURL": "https://" + "fir-pucpr-d6409" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-d6409.appspot.com",
    "messagingSenderId": "474268731285",
    "appId": "1:474268731285:web:40de81e8600e4820d9d89c",
    "measurementId": "G-FKSELZ7WL6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() #solicitando autentificação

# Autenticando credenciais do usuário
print('---------- LOGIN ----------')
user = input("Digite seu e-mail: ")
passwordUser = input("Digite sua senha: ")
status = auth.sign_in_with_email_and_password(user, passwordUser)

# Verificando o email
idToken = status["idToken"]
auth.send_email_verification(idToken)
info = auth.get_account_info(idToken)
users = info["users"]
verifyEmail = users[0]["emailVerified"]

if verifyEmail:
    print('Você está autenticado!')
    # Coletanto data e hora do acesso
    data_atual = datetime.now()
    acesso = data_atual.strftime(f'Acesso do email {user} na data: %d/%m/%Y, e hora: %H:%M \n')

    # Criando arquivo como apenas leitura
    arquivo = open("acesso.txt", 'r')

    # Modifica a permissão do arquivo para leitura, escrita e execução
    if os.path.isfile('acesso.txt'):
        os.chmod("acesso.txt", stat.S_IRWXU)

    # Abrindo o arquivo para escrita
    arquivo = open("acesso.txt", 'a') # a de append, para adicionar todos os horários de acesso sem subistituir

    # Fornecendo informações de ultimo acesso (email, data e hora);
    arquivo.write(acesso)

    # Fecha o arquivo
    arquivo.close()

    # Modifica o arquivo apenas para leitura
    os.chmod("acesso.txt", stat.S_IRUSR)










