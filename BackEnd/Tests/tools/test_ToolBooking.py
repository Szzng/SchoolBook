from random import randint

from django.test import TestCase
from faker import Faker

from Tests.Factories.ToolBookingfactory import ToolBookingFactory
from Tests.Factories.Toolfactory import ToolFactory
from accounts.models import School


class ToolBookingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')

        cls.school = School.objects.create(name=cls.faker.name())
        cls.toolQuantity = randint(10, 200)
        cls.tool = ToolFactory(school=cls.school, quantity=cls.toolQuantity)
        cls.booker = cls.faker.name()
        cls.date = cls.faker.date()

        cls.createUrl = '/api/tools/'
        cls.retrieveUrl = f'/api/tools/{cls.tool.name}/{cls.date}/'

        # cls.destroyUrl = f'/api/tools/{}'
        # cls.LeftRetrieveUrl = f'/api/tools/'

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
        self.assertNotEqual(response.data, postData)

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
        self.assertEqual(response.data, postData)

    def test_toolBooking_올바른_학교_링크로_접속하지_않은_사용자는_날짜별_예약을_조회할_수_없다(self):
        ToolBookingFactory.create_batch(10, **{'tool': self.tool, 'date': self.date})

        response = self.client.get(self.retrieveUrl)

        self.assertEqual(response.status_code, 401)

    def test_toolBooking_올바른_학교_링크로_접속한_사용자는_날짜별_예약을_조회할_수_있다(self):
        toolBookings = ToolBookingFactory.create_batch(10, **{'tool': self.tool, 'date': self.date})

        data = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for booking in toolBookings:
            data[booking.period].append({
                'id': booking.id,
                'booker': booking.booker,
                'quantity': booking.quantity
            })

        response = self.client.get(self.retrieveUrl,
                                   **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)
