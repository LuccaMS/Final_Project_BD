import Conexao

def consulta1():
    consulta1_query = """SELECT id_cliente, nome_cliente, SUM(valor_nota_fiscal) as total_gasto 
                        FROM CLIENTE INNER JOIN nota_fiscal 
                        ON nota_fiscal.fk_Cliente_id_cliente = cliente.id_cliente GROUP BY nome_cliente"""

    Conexao.cr.execute(consulta1_query)
    clientes = Conexao.cr.fetchall()
    return clientes

def consulta3():
    consulta3_query = """SELECT id_maquina, data,descricao_maquina, id_sensor,descricao_sensor, min(medida) as minimo, un_medida
                        FROM MAQUINA INNER JOIN Escala ON escala.fk_Maquina_id_maquina = maquina.id_maquina
                        INNER JOIN  Sensor ON maquina.id_maquina = sensor.fk_Maquina_id_maquina
                        WHERE data BETWEEN '2022-01-01 08:30:01'  and '2022-03-01 08:30:01'
                        GROUP BY un_medida"""
    
    Conexao.cr.execute(consulta3_query)
    maquinas = Conexao.cr.fetchall()
    return maquinas

def consulta2():
    consulta2_query = """SELECT id_fornecedor, nome_fornecedor,avg(valor) as media
                            FROM fornecedor 
                            INNER JOIN Fornece ON fornecedor.id_fornecedor = fornece.fk_Fornecedor_id_fornecedor
                            INNER JOIN Obra_Prima ON obra_prima.id_obra_prima = fornece.fk_Obra_Prima_id_obra_prima
                            GROUP BY nome_fornecedor
                       """

    Conexao.cr.execute(consulta2_query)
    fornecedores = Conexao.cr.fetchall()
    return fornecedores

