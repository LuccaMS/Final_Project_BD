import Conexao
import mysql.connector

def delete_tipo_produto(descricao):
    delete_query = f"DELETE FROM tipo_produto WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Tipo produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_produto(descricao):
    delete_query = f"DELETE FROM produto WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_cliente(nome_cliente):
    delete_query = f"DELETE FROM cliente WHERE nome_cliente = '{nome_cliente}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_fornecedor(nome_fornecedor):
    delete_query = f"DELETE FROM cliente WHERE nome_fornecedor = '{nome_fornecedor}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_funcionario(nome):
    delete_query = f"DELETE FROM funcionario WHERE nome = '{nome}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_maquina(descricao):
    delete_query = f"DELETE FROM maquina WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_obra_prima(descricao):
    delete_query = f"DELETE FROM obra_prima WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_sensor(descricao):
    delete_query = f"DELETE FROM sensor WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def delete_tipo_sensor(descricao):
    delete_query = f"DELETE FROM tipo_sensor WHERE descricao = '{descricao}'"
    #Conexao.cr.commit()
    try: 
        Conexao.cr.execute(delete_query)
        Conexao.cnx.commit()
        print("Produto deletado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()