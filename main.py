from faker import Faker
import Create
import Read
import Delete
if __name__ == '__main__':
    fake = Faker()

    #Create.create_cliente('74.708.966/0001-14',fake.name())
    #Create.create_tipo_produto('Panela')
    Create.create_produto('Cadeira de vidro',88.3,15)
    #teste = Read.read_produto()
    #print(type(teste[1]))
    #print(teste[1])
    #Delete.delete_tipo_produto()


    



