import factory
from tools.models import ToolBooking


class ToolBookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToolBooking
    date = factory.Faker('date_object')
    period = factory.Faker('pyint', min_value=1, max_value=6)
    booker = factory.Faker('word')
    quantity = factory.Faker('pyint', min_value=0, max_value=1000)
