import factory
from accounts.models import School


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = School