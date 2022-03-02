import mysql.connector
from mysql.connector import errorcode


try: cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="trabalho_final") 
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha inválidos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)
else:
    print("Conexão realizada com sucesso")
    cr = cnx.cursor()
