from datetime import datetime
from faker import Faker
import Create
import Read
import Delete
import Read_Where
if __name__ == '__main__':
    fake = Faker()

    #print(Read.read_cliente())
    descricao_tipo_produto = fake.text(max_nb_chars=20)
    descricao_da_maquina = fake.text(max_nb_chars=20)
    descricao_do_produto = fake.text(max_nb_chars=20)
    nome_funcionario = fake.name()

    Create.create_funcionario(nome_funcionario,"430.786.350-07")
    Create.create_cliente("97.246.631/0001-27",fake.name())
    Create.create_tipo_produto(descricao_tipo_produto)
    id_tipo_produto_recem_criado = Read_Where.read_tipo_produto_descricao(descricao_tipo_produto)[0][0]
    Create.create_produto(descricao_do_produto,150,id_tipo_produto_recem_criado)
    id_produto_recem_criado = Read_Where.read_produto_descricao(descricao_do_produto)[0][0]
    Create.create_maquina(descricao_da_maquina,id_produto_recem_criado)
    Create.create_escala(datetime.now(),Read_Where.read_maquina_descricao(descricao_da_maquina)[0][0],Read_Where.read_funcionario_nome(nome_funcionario)[0][0])

    
    

    



