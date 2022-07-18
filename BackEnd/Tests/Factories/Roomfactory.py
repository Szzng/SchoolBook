import factory
from factory import SubFactory
from faker import Faker

from Tests.Factories.Userfactory import UserFactory
from rooms.models import Room, RoomBooking, EmptyTimeTable

faker = Faker('ko_KR')

class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Room

    school = SubFactory(UserFactory)
    name = faker.name()[:5]

class EmptyTimeTableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmptyTimeTable

    room = SubFactory(RoomFactory)
    weekday = factory.Faker('pyint', min_value=0, max_value=4)
    period = factory.Faker('pyint', min_value=1, max_value=6)

class RoomBookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoomBooking

    timetable = SubFactory(EmptyTimeTableFactory)
    date = factory.Faker('date_object')
    booker = faker.name()[:5]