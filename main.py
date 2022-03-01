from faker import Faker
import Create
if __name__ == '__main__':
    fake = Faker()

    Create.create_cliente('74.708.966/0001-14',fake.name())



