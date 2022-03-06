
import Conexao
import mysql.connector

def create_produto(descricao,valor,fk_Tipo_Produto_id_tipo_produto):
    create_produto_query = f"INSERT INTO produto (descricao_produto,valor_produto,fk_Tipo_Produto_id_tipo_produto) VALUES ('{descricao}','{valor}','{fk_Tipo_Produto_id_tipo_produto}')"
    try:
        Conexao.cr.execute(create_produto_query)
        Conexao.cnx.commit()
        print("Produto criado com sucesso")
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


def create_cliente(cnpj,nome):
    create_cliente_query =  f"INSERT INTO cliente (cnpj_cliente,nome_cliente) VALUES ('{cnpj}','{nome}')"
    try:
        Conexao.cr.execute(create_cliente_query)
        Conexao.cnx.commit()
        return "Cliente criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

    
def create_nota_fiscal(desconto,valor,qtd,fk_Cliente_id_cliente,fk_Obra_Prima_id_obra_prima,dt_pgt_transacao, data):
    create_nota_fiscal_query = f"INSERT INTO nota_fiscal (desconto,valor_nota_fiscal,qtd,fk_Cliente_id_cliente,fk_Obra_Prima_id_obra_prima,dt_pgt_transacao,data) VALUES ('{desconto}','{valor}','{qtd}','{fk_Cliente_id_cliente}','{fk_Obra_Prima_id_obra_prima}','{dt_pgt_transacao}','{data}')"
    try:
        Conexao.cr.execute(create_nota_fiscal_query)
        Conexao.cnx.commit()
        return "Nota fiscal criada com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()
    
def obra_prima(descricao_obra_prima,valor):
    create_obra_prima_query = f"INSERT INTO obra_prima (descricao_obra_prima,valor) VALUES ('{descricao_obra_prima}','{valor}')"
    try:
        Conexao.cr.execute(create_obra_prima_query)
        Conexao.cnx.commit()
        return "Obra prima criada com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def create_fornecedor(cnpj_fornecedor,nome_fornecedor,endereco_fornecedor):
    create_fornecedor_query = f"INSERT INTO fornecedor (cnpj_fornecedor,nome_fornecedor,endereco_fornecedor) VALUES ('{cnpj_fornecedor}','{nome_fornecedor}','{endereco_fornecedor}')"
    try:
        Conexao.cr.execute(create_fornecedor_query)
        Conexao.cnx.commit()
        return "Fornecedor criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def create_tipo_produto(descricao_tipo_produto):
    create_tipo_produto_query = f"INSERT INTO tipo_produto (descricao_tipo_produto) VALUES ('{descricao_tipo_produto}')"
    try:
        Conexao.cr.execute(create_tipo_produto_query)
        Conexao.cnx.commit()
        return "Tipo produto criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def create_tipo_sensor(descricao_tipo_sensor):
    create_tipo_sensor = f"INSERT INTO tipo_sensor (descricao_tipo_sensor) VALUES ('{descricao_tipo_sensor}')"
    try:
        Conexao.cr.execute(create_tipo_sensor)
        Conexao.cnx.commit()
        return "Tipo sensor criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()
    

def create_maquina(descricao_maquina,fk_Produto_id_produto):
    create_maquina_query = f"INSERT INTO maquina (descricao_maquina,fk_Produto_id_produto) VALUES ('{descricao_maquina}','{fk_Produto_id_produto}')"
    try:
        Conexao.cr.execute(create_maquina_query)
        Conexao.cnx.commit()
        return "Maquina criada com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


def create_escala(data,fk_Maquina_id_maquina,fk_Funcionario_id_funcionario):
    create_escala_query = f"INSERT INTO escala (data,fk_Maquina_id_maquina,fk_Funcionario_id_funcionario) VALUES ('{data}','{fk_Maquina_id_maquina}','{fk_Funcionario_id_funcionario}')"
    try:
        Conexao.cr.execute(create_escala_query)
        Conexao.cnx.commit()
        return "Escala criada com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()


def create_funcionario(nome,cpf):
    create_funcionario_query = f"INSERT INTO funcionario (nome,cpf) VALUES ('{nome}','{cpf}')"
    try:
        Conexao.cr.execute(create_funcionario_query)
        Conexao.cnx.commit()
        return "Funcionario criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def create_sensor(descricao_sensor,un_medida,fk_Tipo_Sensor_id_tipo_sensor,fk_Maquina_id_maquina,medida):
    create_sensor_query = f"INSERT INTO sensor (descricao_sensor,un_medida,fk_Tipo_Sensor_id_tipo_sensor,fk_Maquina_id_maquina,medida) VALUES ('{descricao_sensor}','{un_medida}','{fk_Tipo_Sensor_id_tipo_sensor}','{fk_Maquina_id_maquina}','{medida}')"
    try:
        Conexao.cr.execute(create_sensor_query)
        Conexao.cnx.commit()
        return "Sensor criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

