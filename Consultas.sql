#Primeira consulta
SELECT id_cliente, nome_cliente, SUM(valor_nota_fiscal) as total_gasto
FROM CLIENTE
INNER JOIN nota_fiscal ON nota_fiscal.fk_Cliente_id_cliente = cliente.id_cliente
GROUP BY nome_cliente;

#Segunda consulta
SELECT id_fornecedor, nome_fornecedor,avg(valor) as media
FROM fornecedor 
INNER JOIN Fornece ON fornecedor.id_fornecedor = fornece.fk_Fornecedor_id_fornecedor
INNER JOIN Obra_Prima ON obra_prima.id_obra_prima = fornece.fk_Obra_Prima_id_obra_prima
GROUP BY nome_fornecedor;

#Terceira Consulta
SELECT descricao_maquina,data, id_sensor, min(medida) as maximo, un_medida
FROM MAQUINA INNER JOIN Escala ON escala.fk_Maquina_id_maquina = maquina.id_maquina
INNER JOIN  Sensor ON maquina.id_maquina = sensor.fk_Maquina_id_maquina
WHERE data BETWEEN '2022-01-01 08:30:01'  and '2022-03-01 08:30:01'
GROUP BY un_medida;

SELECT * FROM funcionario