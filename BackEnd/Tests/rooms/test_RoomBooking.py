import random
from random import randint
from rest_framework.test import APITestCase
from faker import Faker
from Tests.Factories.Roomfactory import RoomFactory, RoomBookingFactory, EmptyTimeTableFactory
from accounts.models import School
from rooms.models import RoomBooking, AvailableEvent, Room


class RoomBookingTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')

        cls.school = School.objects.create(name=cls.faker.name())
        cls.testName = cls.faker.name()[:5]
        cls.timetable = {
            0: ['', '', '', '', '', ''],
            1: ['', '', '', '', '', ''],
            2: ['', '', '', '', '', ''],
            3: ['', '', '', '', '', ''],
            4: ['', '', '', '', '', '']
        }
        cls.date = cls.faker.date()
        cls.createUrl = '/api/rooms/'

    def setUp(self):
        self.client.post("/api/rooms/setting/",
                         {'room': self.testName, 'timetable': self.timetable},
                         format='json',
                         **{'HTTP_AUTHORIZATION': self.school.code})

    '''CRUD TEST'''

    def test_roomBooking_올바른_학교_링크로_접속하지_않은_사용자는_교실_예약을_할_수_없다(self):
        postData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': 6,
            'booker': self.faker.name()[:4],
            'password': '0000'
        }

        response = self.client.post(self.createUrl, postData)

        self.assertEqual(response.status_code, 401)

    def test_roomBooking_올바른_학교_링크로_접속한_사용자는_교실_예약을_할_수_있다(self):
        postData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': 6,
            'booker': self.faker.name()[:4],
            'password': '0000'
        }

        response = self.client.post(self.createUrl, postData,
                                    **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 201)

    def test_roomBooking_이미_예약된_시간에는_교실_예약을_할_수_없다(self):
        firstData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': 6,
            'booker': self.faker.name()[:4],
            'password': '0000'
        }
        response1 = self.client.post(self.createUrl, firstData,
                                     **{'HTTP_AUTHORIZATION': self.school.code})

        secondData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': 6,
            'booker': self.faker.name(),
            'password': '0000'
        }
        response2 = self.client.post(self.createUrl, secondData,
                                     **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertIn('이미 예약 완료된 시간입니다.', response2.data['detail'])

    def test_roomBooking_올바른_학교_링크로_접속하지_않은_사용자는_날짜별_예약을_조회할_수_없다(self):
        room = RoomFactory()
        bookings = {}
        for i in range(1, 7):
            timetable = EmptyTimeTableFactory(room=room, period=i)
            booking = RoomBookingFactory(timetable=timetable, date=self.date)
            bookings[i] = {'id': booking.id, 'booker': booking.booker}

        response = self.client.get(f'/api/rooms/{timetable.room.name}/{self.date}/')

        self.assertEqual(response.status_code, 401)
        self.assertNotEqual(response.data, bookings)

    def test_roomBooking_올바른_학교_링크로_접속한_사용자는_날짜별_예약을_조회할_수_있다(self):
        room = RoomFactory()
        bookings = {}
        for i in range(1, 7):
            timetable = EmptyTimeTableFactory(room=room, period=i)
            booking = RoomBookingFactory(timetable=timetable, date=self.date)
            bookings[i] = {'id': booking.id, 'booker': booking.booker}

        response = self.client.get(f'/api/rooms/{room.name}/{self.date}/',
                                   **{'HTTP_AUTHORIZATION': room.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, bookings)

    def test_roomBooking_올바른_학교_링크로_접속하지_않은_사용자는_예약을_취소할_수_없다(self):
        booking = RoomBookingFactory(password='1111')

        response = self.client.delete(f'/api/rooms/{booking.id}/',
                                      data={'password': '1111'})

        self.assertEqual(response.status_code, 401)
        self.assertTrue(RoomBooking.objects.filter(id=booking.id).exists())

    def test_roomBooking_예약_비밀번호가_틀리면_예약을_취소할_수_없다(self):
        booking = RoomBookingFactory(password='1233')

        response = self.client.delete(f'/api/rooms/{booking.id}/',
                                      data={'password': '1111'},
                                      **{'HTTP_AUTHORIZATION': booking.timetable.room.school.code})

        self.assertEqual(response.status_code, 400)
        self.assertTrue(RoomBooking.objects.filter(id=booking.id).exists())

    def test_roomBooking_예약_비밀번호가_일치하면_예약을_취소할_수_있다(self):
        booking = RoomBookingFactory(password='1111')

        response = self.client.delete(f'/api/rooms/{booking.id}/',
                                      data={'password': '1111'},
                                      **{'HTTP_AUTHORIZATION': booking.timetable.room.school.code})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(RoomBooking.objects.filter(id=booking.id).exists())

    def test_roomBooking_올바른_학교_링크로_접속한_사용자는_월별_예약_가능한_이벤트를_조회할_수_있다(self):
        response = self.client.get(f'/api/rooms/events/{self.testName}/{self.date}/',
                                   **{'HTTP_AUTHORIZATION': self.school.code})
        events = AvailableEvent.objects.filter(
            timetable__room=Room.objects.get(school=self.school.code, name=self.testName).id,
            start__contains=self.date[:7]
        ).order_by('start').values('name', 'start')

        idx = randint(0, len(events) - 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(events[idx], response.data[idx])

    '''Validation TEST'''

    def test_roomBooking_period는_1_이상_6_이하의_수이다(self):
        postData = {
            'room': self.testName,
            'date': '2022-07-18',
            'booker': self.faker.name()[:4],
            'password': '0000'
        }

        wrongPeriod = randint(7, 10)
        rightPeriod = randint(1, 6)

        postData['period'] = wrongPeriod
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['period'] = rightPeriod
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertIn('예약 교시를 확인하세요.', wrongResponse.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)

    def test_roomBooking_예약자는_4글자_이하이어야_한다(self):
        postData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': randint(1, 6),
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

    def test_roomBooking_비밀번호는_4자리의_숫자로_이루어져야_한다(self):
        postData = {
            'room': self.testName,
            'date': '2022-07-18',
            'period': randint(1, 6),
            'booker': self.faker.name()[:4]
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

    def test_roomBooking_날짜는_형식을_지켜야_한다(self):
        postData = {
            'room': self.testName,
            'period': randint(1, 6),
            'booker': self.faker.name()[:4],
            'password': '0000'
        }

        wrongDate = random.choice(
            ['2022년 7월 18일', '2022.7.18.', '220718', '2022/7/18, 2022/07/18', '07-18', '22-07-18'])
        rightDate = '2022-07-18'

        postData['date'] = wrongDate
        wrongResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        postData['date'] = rightDate
        rightResponse = self.client.post(self.createUrl, postData,
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(wrongResponse.status_code, 400)
        self.assertIn('날짜 형식이 올바르지 않습니다.', wrongResponse.data['detail'])
        self.assertEqual(rightResponse.status_code, 201)
