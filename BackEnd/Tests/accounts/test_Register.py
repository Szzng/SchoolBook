from rest_framework.test import APITestCase
from faker import Faker
from accounts.models import School, generate_school_code
from Tests.Factories.Userfactory import UserFactory
from django.db.utils import IntegrityError


class RegisterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.UserModel = School
        cls.faker = Faker()
        cls.testName = cls.faker.word()
        cls.registerUrl = "/api/accounts/register/"

    def test_register_사용자는_회원가입을_할_수_있다(self):
        response = self.client.post(self.registerUrl, {"name": self.testName})
        self.assertTrue(self.UserModel.objects.filter(name=self.testName).exists())
        code = self.UserModel.objects.get(name=self.testName).code
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {
            'name': self.testName,
            'code': code
        })

    def test_register_학교_코드는_중복될_수_없다(self):
        alreadyExistsCode = generate_school_code()
        UserFactory(name=self.testName, code=alreadyExistsCode)
        self.assertTrue(
            self.UserModel.objects.filter(code=alreadyExistsCode).exists()
        )

        with self.assertRaises(IntegrityError) as context:
            UserFactory(name=self.testName, code=alreadyExistsCode)
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_register_학교_이름은_3글자_이상이어야_한다(self):
        nameLess3letters = '2자'
        nameOver3lertters = '3글자'

        response1 = self.client.post(self.registerUrl, {"name": nameLess3letters})
        response2 = self.client.post(self.registerUrl, {"name": nameOver3lertters})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 201)
        self.assertFalse(self.UserModel.objects.filter(name=nameLess3letters).exists())
        self.assertTrue(self.UserModel.objects.filter(name=nameOver3lertters).exists())

    def test_register_학교_이름은_특수문자를_포함하지_않아야_한다(self):
        nameWithSpecialCharacter = '승쨩초등학교123@'
        nameWithOutSpecialCharacter = '승쨩초등학교123'

        response1 = self.client.post(self.registerUrl, {"name": nameWithSpecialCharacter})
        response2 = self.client.post(self.registerUrl, {"name": nameWithOutSpecialCharacter})

        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response2.status_code, 201)
        self.assertFalse(self.UserModel.objects.filter(name=nameWithSpecialCharacter).exists())
        self.assertTrue(self.UserModel.objects.filter(name=nameWithOutSpecialCharacter).exists())
