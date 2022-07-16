from django.test import TestCase
from faker import Faker
from tools.models import Tool


class ToolTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Model = Tool
        cls.faker = Faker()
        cls.testName = cls.faker.word()
        cls.registerUrl = "/api/accounts/register/"
