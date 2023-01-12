import factory
from factory.django import DjangoModelFactory


class PhoneCodeFactory(DjangoModelFactory):
    country = factory.Faker("country")
    code = factory.Faker("country_calling_code")

    class Meta:
        model = "shared.PhoneCode"
