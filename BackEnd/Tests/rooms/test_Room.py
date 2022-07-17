from django.test import TestCase
from faker import Faker
from Tests.Factories.Roomfactory import RoomFactory
from accounts.models import School
from rooms.models import Room


class RoomTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')

        cls.school = School.objects.create(name=cls.faker.name())
        cls.otherSchool = School.objects.create(name=cls.faker.name())
        cls.testName = cls.faker.name()[:5]
        cls.timetable = {
            0: ['', '', '', '', '', ''],
            1: ['', '', '', '', '', ''],
            2: ['', '', '', '', '', ''],
            3: ['', '', '', '', '', ''],
            4: ['', '', '', '', '', '']
        }

        cls.listCreateUrl = "/api/rooms/setting/"
        cls.destoryUrl = "/api/rooms/setting/destroy/"

    '''CRUD TEST'''

    def test_room_올바른_학교_링크로_접속하지_않은_사용자는_새로운_교실을_생성할_수_없다(self):
        data = {'room': self.testName, 'timetable': self.timetable}

        response1 = self.client.post(self.listCreateUrl, data, content_type='application/json')
        response2 = self.client.post(self.listCreateUrl, data, content_type='application/json',
                                     **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response1.status_code, 401)
        self.assertFalse(Room.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    def test_room_올바른_학교_링크로_접속한_사용자는_새로운_교실을_생성할_수_있다(self):
        data = {'room': self.testName, 'timetable': self.timetable}

        response = self.client.post(self.listCreateUrl, data,
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Room.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    def test_room_올바른_학교_링크로_접속하지_않은_사용자는_교실_목록을_조회할_수_없다(self):
        rooms = RoomFactory.create_batch(10, school=self.school)
        roomsList = []
        for room in rooms:
            roomsList.append(dict([('school', self.school.name), ('name', room.name)]))
        roomsList = sorted(roomsList, key=lambda x: x['name'])

        response1 = self.client.get(self.listCreateUrl)
        response2 = self.client.get(self.listCreateUrl,
                                    **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response1.status_code, 401)
        self.assertEqual(response2.status_code, 200)
        self.assertNotEqual(response1.data, roomsList)
        self.assertNotEqual(response2.data, roomsList)

    def test_room_올바른_학교_링크로_접속한_사용자는_교실_목록을_조회할_수_있다(self):
        rooms = RoomFactory.create_batch(10, school=self.school)
        roomsList = []
        for room in rooms:
            roomsList.append(dict([('school', self.school.name), ('name', room.name)]))
        roomsList = sorted(roomsList, key=lambda x: x['name'])

        response = self.client.get(self.listCreateUrl,
                                   **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, roomsList)

    def test_room_올바른_학교_링크로_접속하지_않은_사용자는_교실을_삭제할_수_없다(self):
        room = RoomFactory()

        response = self.client.delete(self.destoryUrl, data={'room': room.name},
                                      content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertTrue(Room.objects.filter(
            school=room.school.code,
            name=room.name
        ).exists())

    def test_room_올바른_학교_링크로_접속한_사용자는_교실을_삭제할_수_있다(self):
        room = RoomFactory()

        response = self.client.delete(self.destoryUrl, data={'room': room.name},
                                      content_type='application/json',
                                      **{'HTTP_AUTHORIZATION': room.school.code})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Room.objects.filter(
            school=room.school.code,
            name=room.name
        ).exists())

    '''Validation TEST'''

    def test_room_학교_코드_내에서_교실_이름은_중복될_수_없다(self):
        room = RoomFactory()
        self.assertTrue(
            Room.objects.filter(school=room.school.code, name=room.name).exists()
        )

        response = self.client.post(self.listCreateUrl,
                                    {'room': room.name, 'timetable': self.timetable},
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': room.school.code})

        self.assertEqual(response.status_code, 400)
        self.assertIn('이미 등록된 이름입니다.', response.data['detail'])

    def test_room_학교_코드가_다르면_교실_이름은_중복될_수_있다(self):
        room = RoomFactory()
        self.assertTrue(
            Room.objects.filter(school=room.school.code, name=room.name).exists()
        )

        response = self.client.post(self.listCreateUrl,
                                    {'room': room.name, 'timetable': self.timetable},
                                    content_type='application/json',
                                    **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 201)

    def test_room_교실_이름은_5글자_이하이어야_한다(self):
        name5letters = '다섯글자임'
        nameOver5lertters = '여섯글자임다'

        rightResponse = self.client.post(self.listCreateUrl,
                                         {'room': name5letters, 'timetable': self.timetable},
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': self.school.code})
        wrongResponse = self.client.post(self.listCreateUrl,
                                         {'room': nameOver5lertters, 'timetable': self.timetable},
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(wrongResponse.status_code, 400)
        self.assertTrue(Room.objects.filter(school=self.school.code, name=name5letters).exists())
        self.assertFalse(Room.objects.filter(school=self.school.code, name=nameOver5lertters).exists())

    def test_room_교실_이름은_특수문자를_포함하지_않아야_한다(self):
        nameWithOutSpecialCharacter = '교실123'
        nameWithSpecialCharacter = '교실12@'

        rightResponse = self.client.post(self.listCreateUrl,
                                         {'room': nameWithOutSpecialCharacter, 'timetable': self.timetable},
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': self.school.code})
        wrongResponse = self.client.post(self.listCreateUrl,
                                         {'room': nameWithSpecialCharacter, 'timetable': self.timetable},
                                         content_type='application/json',
                                         **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(rightResponse.status_code, 201)
        self.assertEqual(wrongResponse.status_code, 400)
        self.assertTrue(Room.objects.filter(school=self.school.code, name=nameWithOutSpecialCharacter).exists())
        self.assertFalse(Room.objects.filter(school=self.school.code, name=nameWithSpecialCharacter).exists())
