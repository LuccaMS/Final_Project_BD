import Conexao
import mysql.connector

def delete_tipo_produto():
    delete_tipo_produto_query = "DELETE FROM tipo_produto WHERE id_tipo_produto = 1"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_tipo_produto_query)
        Conexao.cnx.commit()
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


