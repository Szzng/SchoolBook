import factory
from tools.models import Tool


class ToolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tool

    name = factory.Faker('word')
    quantity = factory.Faker('pyint', min_value=0, max_value=1000)
    place = factory.Faker('word')