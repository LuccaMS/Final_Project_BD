import Conexao
import mysql.connector

def update_produto(id,valor):
    update_query = "update produto set valor = {valor} where id_produto = {id}"
    

    try: 
        Conexao.cr.execute(update_query)
        Conexao.cnx.commit()
        print("Produto atualizado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


def update_obra_prima(id,valor):
    update_query = "update obra_prima set valor = {valor} where id_obra_prima = {id}"
    try: 
        Conexao.cr.execute(update_query)
        Conexao.cnx.commit()
        print("Obra prima atualizado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


