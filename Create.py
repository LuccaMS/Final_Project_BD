
import Conexao

def create_produto(dt_pgt_transacao,desconto,juros,valor,qtd,data):
    return "nothing"

def create_cliente(cnpj,nome):
    create_cliente_query =  f"INSERT INTO cliente (cnpj_cliente,nome_cliente) VALUES ('{cnpj}','{nome}')"
    Conexao.cr.execute(create_cliente_query)
    Conexao.cnx.commit()
    return "Cliente criado com sucesso"
    

def create_nota_fiscal(desconto,juros,valor,qtd,fk_Cliente_id_cliente,fk_Obra_Prima_id_obra_prima):
    return "nothing"

def obra_prima(tipo_obra_prima,descricao,valor,fk_Nota_Fiscal_id_transacao):
    return "nothing"

def create_fornecedor(cnpj_fornecedor,nome_fornecedor,endereco_fornecedor):
    return "nothing"

def create_tipo_produto(descricao):
    return "nothing"

def create_tipo_sensor(descricao):
    return "nothing"

def create_maquina(descricao,fk_Produto_id_produto):
    return "nothing"

def create_escala(data,fk_Maquina_id_maquina,fk_Funcionario_id_funcionario):
    return "nothing"

def create_funcionario(nome,cpf):
    return "nothing"

def create_sensor(descricao,un_medida,):
    return "nothing"

