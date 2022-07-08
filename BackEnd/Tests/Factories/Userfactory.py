import factory
import accounts.models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = accounts.models.School