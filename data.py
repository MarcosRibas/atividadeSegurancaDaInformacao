from datetime import datetime



data_atual = datetime.now()
acesso = data_atual.strftime('Acesso na data: %d/%m/%Y, e hora: %H:%M \n')

print(acesso)

