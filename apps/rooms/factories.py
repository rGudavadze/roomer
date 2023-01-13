import factory
from factory.django import DjangoModelFactory


class InventoryFactory(DjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = "rooms.Inventory"


class RoomFactory(DjangoModelFactory):
    name = factory.Faker("word")
    seats = factory.Faker("pyint", max_value=999)

    class Meta:
        model = "rooms.Room"
