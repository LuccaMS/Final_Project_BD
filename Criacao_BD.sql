/* Logico_Trabalho_Final: */

CREATE TABLE Fornecedor (
    id_fornecedor INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    cnpj_fornecedor VARCHAR(18),
    nome_fornecedor VARCHAR(60),
    endereco_fornecedor VARCHAR(60)
);

CREATE TABLE Cliente (
    id_cliente INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    cnpj_cliente VARCHAR(18),
    nome_cliente VARCHAR(60)
);

CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    descricao_produto VARCHAR(600),
    valor_produto decimal,
    fk_Tipo_Produto_id_tipo_produto INTEGER
);

CREATE TABLE Maquina (
    id_maquina INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    descricao_maquina VARCHAR(600),
    fk_Produto_id_produto INTEGER
);

CREATE TABLE Sensor (
    descricao_sensor VARCHAR(600),
    fk_Tipo_Sensor_id_tipo_sensor INTEGER,
    id_sensor INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    un_medida VARCHAR(18),
    fk_Maquina_id_maquina INTEGER,
    medida INTEGER
);

CREATE TABLE Obra_Prima (
    descricao_obra_prima VARCHAR(600),
    valor decimal,
    id_obra_prima INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT
);

CREATE TABLE Nota_Fiscal (
    id_nota_fiscal INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    dt_pgt_transacao DATETIME,
    desconto decimal,
    valor_nota_fiscal DECIMAL,
    fk_Cliente_id_cliente INTEGER,
    data datetime,
    qtd INTEGER,
    fk_Obra_Prima_id_obra_prima INTEGER
);

CREATE TABLE Fornece (
    fk_Fornecedor_id_fornecedor INTEGER,
    fk_Obra_Prima_id_obra_prima INTEGER
);

CREATE TABLE Possui (
    fk_Produto_id_produto INTEGER,
    fk_Nota_id_nota_fiscal INTEGER
);

CREATE TABLE Tipo_Sensor (
    id_tipo_sensor INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    descricao_tipo_sensor VARCHAR(600)
);

CREATE TABLE Escala (
    fk_Maquina_id_maquina INTEGER,
    fk_Funcionario_id_funcionario INTEGER,
    data DATETIME PRIMARY KEY
);

CREATE TABLE Funcionario (
    id_funcionario INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    nome VARCHAR(60),
    cpf VARCHAR(14)
);

CREATE TABLE Tipo_Produto (
    id_tipo_produto INTEGER PRIMARY KEY UNIQUE AUTO_INCREMENT,
    descricao_tipo_produto VARCHAR(600)
);
 
ALTER TABLE Produto ADD CONSTRAINT FK_Produto_3
    FOREIGN KEY (fk_Tipo_Produto_id_tipo_produto)
    REFERENCES Tipo_Produto (id_tipo_produto);
 
ALTER TABLE Maquina ADD CONSTRAINT FK_Maquina_2
    FOREIGN KEY (fk_Produto_id_produto)
    REFERENCES Produto (id_produto)
    ON DELETE RESTRICT;
 
ALTER TABLE Sensor ADD CONSTRAINT FK_Sensor_1
    FOREIGN KEY (fk_Maquina_id_maquina)
    REFERENCES Maquina (id_maquina)
    ON DELETE RESTRICT;
 
ALTER TABLE Sensor ADD CONSTRAINT FK_Sensor_4
    FOREIGN KEY (fk_Tipo_Sensor_id_tipo_sensor)
    REFERENCES Tipo_Sensor (id_tipo_sensor);
  
ALTER TABLE Nota_Fiscal ADD CONSTRAINT FK_Nota_Fiscal_2
    FOREIGN KEY (fk_Cliente_id_cliente)
    REFERENCES Cliente (id_cliente);
    
ALTER TABLE nota_fiscal ADD CONSTRAINT FK_Nota_Fiscal_3
	FOREIGN KEY (fk_Obra_Prima_id_obra_prima)
    REFERENCES obra_prima (id_obra_prima);
 
ALTER TABLE Fornece ADD CONSTRAINT FK_Fornece_1
    FOREIGN KEY (fk_Fornecedor_id_fornecedor)
    REFERENCES Fornecedor (id_fornecedor)
    ON DELETE RESTRICT;
 
ALTER TABLE Fornece ADD CONSTRAINT FK_Fornece_2
    FOREIGN KEY (fk_Obra_Prima_id_obra_prima)
    REFERENCES Obra_Prima (id_obra_prima);
 
ALTER TABLE Possui ADD CONSTRAINT FK_Possui_1
    FOREIGN KEY (fk_Produto_id_produto)
    REFERENCES Produto (id_produto)
    ON DELETE SET NULL;
 
ALTER TABLE Possui ADD CONSTRAINT FK_Possui_2
    FOREIGN KEY (fk_Nota_id_nota_fiscal)
    REFERENCES Nota_Fiscal (id_nota_fiscal);
 
ALTER TABLE Escala ADD CONSTRAINT FK_Escala_1
    FOREIGN KEY (fk_Maquina_id_maquina)
    REFERENCES Maquina (id_maquina);
    
ALTER TABLE Escala ADD CONSTRAINT FK_Escala_2
    FOREIGN KEY (fk_Funcionario_id_funcionario)
    REFERENCES Funcionario (id_funcionario);

    
    
    
    
    