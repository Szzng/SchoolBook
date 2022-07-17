import factory
from factory import SubFactory
from faker import Faker

from Tests.Factories.Userfactory import UserFactory
from rooms.models import Room, RoomBooking

faker = Faker('ko_KR')
toolQuantity = faker.pyint(min_value=30, max_value=200)
bookingQuantity = faker.pyint(min_value=1, max_value=toolQuantity)

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    school = SubFactory(UserFactory)
    name = faker.name()[:5]
