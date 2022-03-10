insert into obra_prima (descricao_obra_prima, valor) values ("madeira",300);
insert into obra_prima (descricao_obra_prima, valor) values ("ferro",500);
insert into obra_prima (descricao_obra_prima, valor) values ("trigo",250);
insert into obra_prima (descricao_obra_prima, valor) values ("Feijao",50);

insert into funcionario (cpf,nome) values ('123442345325','maria');
insert into funcionario (cpf,nome) values ('865437643675','jose');
insert into funcionario (cpf,nome) values ('534678654234','vanderson');

insert into tipo_produto (descricao_tipo_produto) values ("Himenaeos dolor pulvinar fusce, amet risus.");
insert into tipo_produto (descricao_tipo_produto) values ("Tellus posuere odio maecenas, sit etiam.");
insert into tipo_produto (descricao_tipo_produto) values ("In quam arcu egestas, dui volutpat.");
insert into tipo_produto (descricao_tipo_produto) values ("Eu egestas sagittis inceptos, tincidunt auctor.");

insert into produto (descricao_produto,	valor_produto, fk_tipo_produto_id_tipo_produto) values ("Malesuada dictum mollis habitant, nisi venenatis.",366,1);
insert into produto (descricao_produto,	valor_produto, fk_tipo_produto_id_tipo_produto) values ("Cursus rutrum viverra enim, conubia volutpat. ",346,2);
insert into produto (descricao_produto,	valor_produto, fk_tipo_produto_id_tipo_produto) values ("Praesent fermentum viverra curae, vehicula ante.",283,3);
insert into produto (descricao_produto,	valor_produto, fk_tipo_produto_id_tipo_produto) values ("Suspendisse ligula commodo phasellus, ultricies morbi.",195,4);
insert into produto (descricao_produto,	valor_produto, fk_tipo_produto_id_tipo_produto) values ("Suspendisse ligula commodo phasellus, ultadwawdawricies adwawd .",380,4);

insert into maquina (descricao_maquina, fk_produto_id_produto) values ("Consequat ornare diam taciti, consequat curae.",1);
insert into maquina (descricao_maquina, fk_produto_id_produto) values ("Ultrices velit elementum tellus, mattis dapibus",2);
insert into maquina (descricao_maquina, fk_produto_id_produto) values ("Lobortis fames donec blandit, pulvinar tellus.",3);
insert into maquina (descricao_maquina, fk_produto_id_produto) values ("Ac vitae dolor etiam, enim integer.",4);
insert into maquina (descricao_maquina, fk_produto_id_produto) values ("Ac vitae dolor etiam, enim kdmawk.",5);

insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (1,1,"2022-02-18 12:54:37");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (2,2,"2022-01-12 07:22:43");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (3,3,"2022-02-20 07:17:30");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (1,2,"2022-01-03 11:32:22");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (2,3,"2022-01-04 03:44:20");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (3,1,"2022-02-17 06:38:45");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (1,3,"2022-02-02 12:25:37");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (4,1,"2022-02-24 09:02:01");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (4,2,"2022-01-24 09:02:01");
insert into escala (fk_maquina_id_maquina,fk_funcionario_id_funcionario,data) values (5,1,"2022-01-25 08:30:01");


insert into cliente (cnpj_cliente, nome_cliente) values ('68.071.434/0001-16','Gilzi');
insert into cliente (cnpj_cliente,nome_cliente) values ('42.996.571/0001-78','Loak');
insert into cliente (cnpj_cliente,nome_cliente) values ('39.898.901/0001-88','Elpeol');
insert into cliente (cnpj_cliente,nome_cliente) values ('72.119.941/0001-50','Esraen');
insert into cliente (cnpj_cliente,nome_cliente) values ('98.071.370/0001-14','Buoraen');
insert into cliente (cnpj_cliente,nome_cliente) values ('09.077.633/0001-72','Preanfa');

insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Manoel Breno João Jesus", "59.234.070/0001-57", "Rua Doutor Jorge");
insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Sebastião Kaique César Peixoto", "96.016.443/0001-40", "Quadra D");
insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Larissa Renata Cecília da Paz", "09.006.083/0001-09", "Rua Amapá");
insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Regina Lavínia Fernanda Monteiro", "72.475.907/0001-18", "Rua Pedro Martins");
insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Teresinha Rafaela Rebeca Lopes", "24.107.094/0001-60", "Rua Topázio");
insert into fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor) values ("Fábio Jorge Lucca Moreira", "37.965.584/0001-40", "Rua das Orquídeas");
insert into nota_fiscal (dt_pgt_transacao, desconto, valor_nota_fiscal, fk_cliente_id_cliente, data, qtd, fk_obra_prima_id_obra_prima) values ("2021-01-03 10:49:31",1.52, 1254,4, "2022-01-05 03:21:38",470,1);

insert into nota_fiscal (dt_pgt_transacao, desconto, valor_nota_fiscal, fk_cliente_id_cliente, data, qtd, fk_obra_prima_id_obra_prima) values ("2022-01-25 06:43:19",1.23,1948,1,"2022-02-10 10:17:44",594,1);
insert into nota_fiscal (dt_pgt_transacao, desconto, valor_nota_fiscal, fk_cliente_id_cliente, data, qtd, fk_obra_prima_id_obra_prima) values ("2022-01-26 03:37:53",1.32, 3436,6, "2022-02-18 01:41:19",335,2);
insert into nota_fiscal (dt_pgt_transacao, desconto, valor_nota_fiscal, fk_cliente_id_cliente, data, qtd, fk_obra_prima_id_obra_prima) values ("2021-01-02 11:51:59",1.45, 2387,3, "2022-02-18 01:05:46",179,3);
insert into nota_fiscal (dt_pgt_transacao, desconto, valor_nota_fiscal, fk_cliente_id_cliente, data, qtd, fk_obra_prima_id_obra_prima) values ("2021-01-02 02:49:31",1.57, 2709,4, "2022-01-05 03:21:38",470,3);

insert into tipo_sensor (descricao_tipo_sensor) values ("Lectus magna dapibus turpis, at eu.");
insert into tipo_sensor (descricao_tipo_sensor) values ("Fames amet potenti luctus, adipiscing placerat.");
insert into tipo_sensor (descricao_tipo_sensor) values ("Inceptos est donec non, ligula dictum.");
insert into tipo_sensor (descricao_tipo_sensor) values ("Sed auctor primis nostra, donec nisl.");

insert into sensor (descricao_sensor,fk_tipo_sensor_id_tipo_sensor,un_medida,medida, fk_maquina_id_maquina) values ("Luctus ornare nulla diam, posuere per.",1,"Kg",29,1);
insert into sensor (descricao_sensor,fk_tipo_sensor_id_tipo_sensor,un_medida,medida, fk_maquina_id_maquina) values ("Risus elementum quisque eleifend, aliquet velit.",2,"C°",19,2);
insert into sensor (descricao_sensor,fk_tipo_sensor_id_tipo_sensor,un_medida,medida, fk_maquina_id_maquina) values ("Tellus magna molestie malesuada, justo quisque.",3,"N/m²",56,3);
insert into sensor (descricao_sensor,fk_tipo_sensor_id_tipo_sensor,un_medida,medida, fk_maquina_id_maquina) values ("Facilisis libero tortor vestibulum, nisl enim.",4,"Pa",12,4);
insert into sensor (descricao_sensor,fk_tipo_sensor_id_tipo_sensor,un_medida,medida, fk_maquina_id_maquina) values ("Facilisis libero tortor vestibulum, nisl enim.",4,"Pa",39,5);

insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (1,1);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (2,2);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (3,3);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (4,4);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (1,2);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (2,3);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (3,4);
insert into possui (fk_produto_id_produto, fk_nota_id_nota_fiscal) values (4,1);

insert into fornece (fk_fornecedor_id_fornecedor,fk_obra_prima_id_obra_prima) values (1,1);
insert into fornece (fk_fornecedor_id_fornecedor,fk_obra_prima_id_obra_prima) values (2,2);
insert into fornece (fk_fornecedor_id_fornecedor,fk_obra_prima_id_obra_prima) values (3,3);
insert into fornece (fk_fornecedor_id_fornecedor,fk_obra_prima_id_obra_prima) values (3,4);
