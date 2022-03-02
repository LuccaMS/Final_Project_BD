
import Conexao
import mysql.connector

def create_produto(desricao,valor,fk_Tipo_Produto_id_tipo_produto):
    create_produto_query = f"INSERT INTO produto (descricao,valor,fk_Tipo_Produto_id_tipo_produto) VALUES ('{desricao}','{valor}','{fk_Tipo_Produto_id_tipo_produto}')"
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

    
def create_nota_fiscal(desconto,juros,valor,qtd,fk_Cliente_id_cliente,fk_Obra_Prima_id_obra_prima):
    create_nota_fiscal_query = f"INSERT INTO nota_fiscal (desconto,juros,valor,qtd,fk_Cliente_id_cliente,fk_Obra_Prima_id_obra_prima) VALUES ('{desconto}','{juros}','{valor}','{qtd}','{fk_Cliente_id_cliente}','{fk_Obra_Prima_id_obra_prima}')"
    try:
        Conexao.cr.execute(create_nota_fiscal_query)
        Conexao.cnx.commit()
        return "Nota fiscal criada com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()
    
def obra_prima(tipo_obra_prima,descricao,valor):
    create_obra_prima_query = f"INSERT INTO obra_prima (tipo_obra_prima,descricao,valor) VALUES ('{tipo_obra_prima}','{descricao}','{valor}')"
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

def create_tipo_produto(descricao):
    create_tipo_produto_query = f"INSERT INTO tipo_produto (descricao) VALUES ('{descricao}')"
    try:
        testee =Conexao.cr.execute(create_tipo_produto_query)
        teste = Conexao.cnx.commit()
        print(testee)
        return "Tipo produto criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

def create_tipo_sensor(descricao):
    create_tipo_sensor = f"INSERT INTO tipo_sensor (descricao) VALUES ('{descricao}')"
    try:
        Conexao.cr.execute(create_tipo_sensor)
        Conexao.cnx.commit()
        return "Tipo sensor criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()
    

def create_maquina(descricao,fk_Produto_id_produto):
    create_maquina_query = f"INSERT INTO maquina (descricao,fk_Produto_id_produto) VALUES ('{descricao}','{fk_Produto_id_produto}')"
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

def create_sensor(descricao,un_medida,fk_Tipo_Sensor_id_tipo_sensor,fk_Maquina_id_maquina):
    create_sensor_query = f"INSERT INTO sensor (descricao,un_medida,fk_Tipo_Sensor_id_tipo_sensor,fk_Maquina_id_maquina) VALUES ('{descricao}','{un_medida}','{fk_Tipo_Sensor_id_tipo_sensor}','{fk_Maquina_id_maquina}')"
    try:
        Conexao.cr.execute(create_sensor_query)
        Conexao.cnx.commit()
        return "Sensor criado com sucesso"
    except mysql.connector.Error as err:
        print(err)
        Conexao.cnx.rollback()

