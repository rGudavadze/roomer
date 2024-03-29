import factory
from factory.django import DjangoModelFactory


class PhoneCodeFactory(DjangoModelFactory):
    country = factory.Faker("country")
    code = factory.Faker("country_calling_code")

    class Meta:
        model = "app_helpers.PhoneCode"


class InventoryFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = "app_helpers.Inventory"
