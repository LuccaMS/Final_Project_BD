import Conexao

def read_produto():
    read_produto_query = "SELECT * FROM produto"
    Conexao.cr.execute(read_produto_query)
    produtos = Conexao.cr.fetchall()
    return produtos

def read_cliente():
    read_clientes_query = "SELECT * FROM cliente"
    Conexao.cr.execute(read_clientes_query)
    clientes = Conexao.cr.fetchall()
    return clientes

def read_tipo_produto():
    read_tipo_produto_query = "SELECT * FROM tipo_produto"
    Conexao.cr.execute(read_tipo_produto_query)
    tipo_produto = Conexao.cr.fetchall()
    return tipo_produto

def read_tipo_sensor():
    read_tipo_sensor_query = "SELECT * FROM tipo_sensor"
    Conexao.cr.execute(read_tipo_sensor_query)
    tipo_sensor = Conexao.cr.fetchall()
    return tipo_sensor

def read_sensor():
    read_sensor_query = "SELECT * FROM sensor"
    Conexao.cr.execute(read_sensor_query)
    sensor = Conexao.cr.fetchall()
    return sensor
    
def read_maquina():
    read_maquina_query = "SELECT * FROM maquina"
    Conexao.cr.execute(read_maquina_query)
    maquina = Conexao.cr.fetchall()
    return maquina

def read_funcionario():
    read_funcionario_query = "SELECT * FROM funcionario"
    Conexao.cr.execute(read_funcionario_query)
    funcionario = Conexao.cr.fetchall()
    return funcionario

def read_fornecedor():
    read_fornecedor_query = "SELECT * FROM fornecedor"
    Conexao.cr.execute(read_fornecedor_query)
    fornecedor = Conexao.cr.fetchall()
    return fornecedor
    
def read_nota_fiscal():
    read_nota_fiscal_query = "SELECT * FROM nota_fiscal"
    Conexao.cr.execute(read_nota_fiscal_query)
    nota_fiscal = Conexao.cr.fetchall()
    return nota_fiscal

def read_obra_prima():
    read_obra_prima_query = "SELECT * FROM obra_prima"
    Conexao.cr.execute(read_obra_prima_query)
    obra_prima = Conexao.cr.fetchall()
    return obra_prima

