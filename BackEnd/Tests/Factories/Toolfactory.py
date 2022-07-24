import factory
from factory import SubFactory
from faker import Faker

from Tests.Factories.Userfactory import UserFactory
from tools.models import Tool, ToolBooking

faker = Faker('ko_KR')
toolQuantity = faker.pyint(min_value=30, max_value=200)
bookingQuantity = faker.pyint(min_value=1, max_value=toolQuantity)

class ToolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tool

    school = SubFactory(UserFactory)
    name = faker.name()[:5]
    quantity = toolQuantity
    place = faker.name()[:5]


class ToolBookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToolBooking

    tool = SubFactory(ToolFactory)
    date = factory.Faker('date_object')
    period = factory.Faker('pyint', min_value=1, max_value=7)
    booker = factory.Faker('word')
    quantity = bookingQuantity
    password = '0000'
