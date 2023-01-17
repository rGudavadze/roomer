import factory
from factory.django import DjangoModelFactory


class RoomFactory(DjangoModelFactory):
    name = factory.Faker("word")
    seats = factory.Faker("pyint", max_value=999)

    class Meta:
        model = "rooms.Room"
