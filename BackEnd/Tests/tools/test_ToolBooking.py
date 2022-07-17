import random
from random import randint

from django.test import TestCase
from faker import Faker

from Tests.Factories.Toolfactory import ToolFactory, ToolBookingFactory
from accounts.models import School
from tools.actions import getLeft
from tools.models import ToolBooking


class ToolBookingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')

        cls.school = School.objects.create(name=cls.faker.name())
        cls.tool = ToolFactory(school=cls.school)
        cls.date = cls.faker.date()

        cls.createUrl = '/api/tools/'
        cls.retrieveUrl = f'/api/tools/{cls.tool.name}/{cls.date}/'
        cls.leftRetrieveUrl = f'/api/tools/left/{cls.tool.name}/{cls.date}/'

    '''CRUD TEST'''

    def test_toolBooking_올바른_학교_링크로_접속하지_않은_사용자는_교구_예약을_할_수_없다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': self.faker.name(),
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }

        response = self.client.post(self.createUrl, postData)

        self.assertEqual(response.status_code, 401)
        self.assertNotEqual(response.data, postData)

    def test_toolBooking_올바른_학교_링크로_접속한_사용자는_교구_예약을_할_수_있다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': self.faker.name(),
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
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

    def test_toolBooking_올바른_학교_링크로_접속하지_않은_사용자는_예약을_취소할_수_없다(self):
        booking = ToolBookingFactory(password='1111')

        response = self.client.delete(f'/api/tools/{booking.id}/',
                                      data={'password': '1111'},
                                      content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertTrue(ToolBooking.objects.filter(id=booking.id).exists())

    def test_toolBooking_예약_비밀번호가_틀리면_예약을_취소할_수_없다(self):
        booking = ToolBookingFactory(password='1111')

        response = self.client.delete(f'/api/tools/{booking.id}/',
                                      data={'password': '0000'},
                                      content_type='application/json',
                                      **{'HTTP_AUTHORIZATION': booking.tool.school.code})

        self.assertEqual(response.status_code, 400)
        self.assertTrue(ToolBooking.objects.filter(id=booking.id).exists())

    def test_toolBooking_예약_비밀번호가_일치하면_예약을_취소할_수_있다(self):
        booking = ToolBookingFactory(password='1111')

        response = self.client.delete(f'/api/tools/{booking.id}/',
                                      data={'password': '1111'},
                                      content_type='application/json',
                                      **{'HTTP_AUTHORIZATION': booking.tool.school.code})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(ToolBooking.objects.filter(id=booking.id).exists())

    def test_toolBooking_예약을_하면_잔여_수량이_감소한다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1'],
            'booker': self.faker.name(),
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }

        beforeLefts = getLeft(self.tool, str(postData['date']) + '-' + '1')
        self.client.post(self.createUrl, postData, **{'HTTP_AUTHORIZATION': self.school.code})
        afterLefts = getLeft(self.tool, str(postData['date']) + '-' + '1')

        self.assertEqual(beforeLefts - postData['quantity'], afterLefts)

    def test_toolBooking_예약을_취소하면_잔여_수량이_증가된다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1'],
            'booker': self.faker.name(),
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }
        self.client.post(self.createUrl, postData, **{'HTTP_AUTHORIZATION': self.school.code})
        beforeLefts = getLeft(self.tool, str(postData['date']) + '-' + '1')
        postData['tool'] = self.tool.id
        postData['period'] = 1
        booking = ToolBooking.objects.get(**postData)
        self.client.delete(f'/api/tools/{booking.id}/',
                           data={'password': '0000'},
                           content_type='application/json',
                           **{'HTTP_AUTHORIZATION': booking.tool.school.code})
        afterLefts = getLeft(self.tool, str(postData['date']) + '-' + '1')

        self.assertEqual(afterLefts, beforeLefts + booking.quantity)

    def test_toolBooking_날짜별_예약_가능한_잔여_수량을_확인할_수_있다(self):
        response = self.client.get(self.leftRetrieveUrl, **{'HTTP_AUTHORIZATION': self.school.code})

        lefts = [0] * 6
        for i in range(6):
            lefts[i] = getLeft(self.tool, str(self.date) + '-' + str(i + 1))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, lefts)

    '''Validation TEST'''

    def test_toolBooking_period는_1_이상_6_이하의_수이다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'booker': self.faker.name(),
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }

        wrongPeriod = ['1', '3', '7']
        rightPeriod = ['1', '2', '4', '6']

        postData['period'] = wrongPeriod
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['period'] = rightPeriod
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertIn('예약 교시를 확인하세요.', wrongResponse.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(rightResponse.data, postData)

    def test_toolBooking_예약자는_4글자_이하이어야_한다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }

        wrongBooker = '4학년7반'
        rightBooker = '4-7'

        postData['booker'] = wrongBooker
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['booker'] = rightBooker
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertIn('예약자는 4글자 이하로 적어주세요.', wrongResponse.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(rightResponse.data, postData)

    def test_toolBooking_대여_수량은_0_이상_잔여_수량_이하이어야_한다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': '4-7-',
            'password': '0000'
        }
        standard = self.tool.quantity
        lessQuantity = randint(-100, 1)
        overQuantity = randint(standard + 1, standard + 100)
        rightQuantity = randint(1, standard + 1)

        postData['quantity'] = lessQuantity
        wrongResponse1 = self.client.post(self.createUrl, postData,
                                          **{'HTTP_AUTHORIZATION': self.school.code})

        postData['quantity'] = overQuantity
        wrongResponse2 = self.client.post(self.createUrl, postData,
                                          **{'HTTP_AUTHORIZATION': self.school.code})

        postData['quantity'] = rightQuantity
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse1.status_code, 400)
        self.assertIn('대여 수량은 0보다 큰 수를 입력해주세요.', wrongResponse1.data['detail'])
        self.assertEqual(wrongResponse2.status_code, 400)
        self.assertIn('대여 가능한 수량을 확인하세요.', wrongResponse2.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(rightResponse.data, postData)

    def test_toolBooking_비밀번호는_4자리의_숫자로_이루어져야_한다(self):
        postData = {
            'tool': self.tool.name,
            'date': self.faker.date(),
            'period': ['1', '2', '3'],
            'booker': '4-7-',
            'quantity': randint(1, self.tool.quantity),
        }

        wrongPassword = random.choice(['123a', 'abc1', '12345', '한글비번', '123456', '한글12'])
        rightPassword = '1234'

        postData['password'] = wrongPassword
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['password'] = rightPassword
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(rightResponse.data, postData)

    def test_toolBooking_날짜는_형식을_지켜야_한다(self):
        postData = {
            'tool': self.tool.name,
            'period': ['1', '2', '3'],
            'booker': '4-7-',
            'quantity': randint(1, self.tool.quantity),
            'password': '0000'
        }

        wrongDate = random.choice(
            ['2022년 7월 17일', '2022.7.17.', '220717', '2022/7/17, 2022/07/17', '07-17', '22-07-17'])
        rightDate = self.faker.date()

        postData['date'] = wrongDate
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['date'] = rightDate
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertIn('날짜 형식이 올바르지 않습니다.', wrongResponse.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(rightResponse.data, postData)
