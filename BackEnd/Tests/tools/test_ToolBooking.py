from random import randint

from django.test import TestCase
from faker import Faker

from Tests.Factories.ToolBookingfactory import ToolBookingFactory
from Tests.Factories.Toolfactory import ToolFactory
from accounts.models import School
from tools.models import Tool, Period


class ToolBookingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')

        cls.school = School.objects.create(name=cls.faker.name())
        cls.toolQuantity = randint(10, 200)
        cls.date = cls.faker.date()
        cls.tool = ToolFactory(school=cls.school, quantity=cls.toolQuantity)
        cls.period = Period.objects.create(school=cls.school, date=cls.date, period=1, id=cls.date + '-' + '1')
        cls.booker = cls.faker.name()

        cls.createUrl = '/api/tools/'
        cls.retrieveUrl = f'/api/tools/{cls.tool.name}/{cls.date}/'

        # cls.destroyUrl = f'/api/tools/{}'
        # cls.availableLeftUrl = f'/api/tools/'

    '''CRUD TEST'''

    def test_toolBooking_올바른_학교_링크로_접속하지_않은_사용자는_교구_예약을_할_수_없다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': self.booker,
            'quantity': randint(1, self.toolQuantity)
        }

        response = self.client.post(self.createUrl, postData)

        self.assertEqual(response.status_code, 401)
        self.assertNotEqual(response.data, {
            'school': self.school.name,
            'tool': self.tool.name,
            'period': postData['period'],
            'quantity': postData['quantity']
        })

    def test_toolBooking_올바른_학교_링크로_접속한_사용자는_교구_예약을_할_수_있다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': self.booker,
            'quantity': randint(1, self.toolQuantity)
        }

        response = self.client.post(self.createUrl, postData,
                                    **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {
            'school': self.school.name,
            'tool': self.tool.name,
            'period': postData['period'],
            'quantity': postData['quantity']
        })

    def test_toolBooking_올바른_학교_링크로_접속하지_않은_사용자는_날짜별_예약을_조회할_수_없다(self):
        ToolBookingFactory(tool=self.tool, period=self.period)

        response = self.client.get(self.retrieveUrl)

        self.assertEqual(response.status_code, 401)
