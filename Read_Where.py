import Conexao
import mysql.connector

def read_tipo_produto_descricao(descricao_tipo_produto):
    read_tipo_produto_query = "SELECT * FROM tipo_produto WHERE descricao_tipo_produto = '" + descricao_tipo_produto + "'"
    try:
        Conexao.cr.execute(read_tipo_produto_query)
        tipo_produto = Conexao.cr.fetchall()
        return tipo_produto
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def read_produto_descricao(descricao_produto):
    read_produto_query = "SELECT * FROM produto WHERE descricao_produto = '" + descricao_produto + "'"
    try:
        Conexao.cr.execute(read_produto_query)
        produto = Conexao.cr.fetchall()
        return produto
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def read_maquina_descricao(descricao_maquina):
    read_maquina_query = "SELECT * FROM maquina WHERE descricao_maquina = '" + descricao_maquina + "'"
    try:
        Conexao.cr.execute(read_maquina_query)
        maquina = Conexao.cr.fetchall()
        return maquina
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def read_funcionario_nome(nome):
    read_funcionario_query = "SELECT * FROM funcionario WHERE nome = '" + nome + "'"
    try:
        Conexao.cr.execute(read_funcionario_query)
        funcionario = Conexao.cr.fetchall()
        return funcionario
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()