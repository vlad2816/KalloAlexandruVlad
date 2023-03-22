from faker import Faker
from faker.providers import automotive
fake = Faker('ro_Ro')
fake.add_provider(automotive)


for i in range(100):
    print(fake.license_plate())
