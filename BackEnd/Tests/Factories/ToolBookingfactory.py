import factory
from tools.models import ToolBooking


class ToolBookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToolBooking

    booker = factory.Faker('word')
    quantity = factory.Faker('pyint', min_value=0, max_value=1000)