import factory
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")

    class Meta:
        model = "users.User"
