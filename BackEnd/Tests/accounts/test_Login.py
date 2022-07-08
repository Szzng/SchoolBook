from django.test import TestCase
from faker import Faker

from accounts.models import School, generate_school_code


class LoginTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.loginUrl = "/api/accounts/login/"
        cls.faker = Faker()
        cls.exactName = cls.faker.word()
        cls.exactCode = generate_school_code()
        cls.user = School.objects.create(name=cls.exactName, code=cls.exactCode)

    def test_login_학교_코드가_포함된_url로_접속하면_로그인_할_수_있다(self):
        response = self.client.get(self.loginUrl + self.exactCode + '/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'name': self.exactName, 'code': self.exactCode})

    def test_login_가입되지_않은_학교_코드로는_로그인_할_수_없다(self):
        unRegisteredCode = generate_school_code()

        response = self.client.get(self.loginUrl + unRegisteredCode + '/')

        self.assertEqual(response.status_code, 401)
