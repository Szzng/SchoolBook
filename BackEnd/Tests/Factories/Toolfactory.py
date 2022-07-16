import factory

from tools.models import Tool


class ToolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tool

    name = factory.Faker('word')
    quantity = factory.Faker('pyint')
    place = factory.Faker('word')