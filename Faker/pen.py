from faker import Faker 
fake = Faker()


print(fake.name())
print(fake.address())
print(fake.profile())
print(fake.text())
print(fake.sentence())
print(fake.country())
print(fake.city())

a_list = ['apple','banana','cherry','dog','fish']
print(fake.sentence(ext_word_list=a_list))

for x in range(10):
    print(fake.name())

fake.seed(2)
print(fake.address())

fake = Faker('de_CH')
for x in range(10):
    print('Name->',fake.name(),'Country->',fake.country(),'Address->',fake.address())

from faker.providers import internet 

fake = Faker()
fake.add_provider(internet)
print(fake.ipv4_private())




