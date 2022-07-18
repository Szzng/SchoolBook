from random import randint

from django.test import TestCase
from faker import Faker
from Tests.Factories.Toolfactory import ToolFactory
from accounts.models import School
from tools.models import Tool


class ToolTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker('ko_KR')
        cls.school = School.objects.create(name=cls.faker.name())
        cls.otherSchool = School.objects.create(name=cls.faker.name())
        cls.testName = cls.faker.name()[:5]
        cls.testQuantity = cls.faker.pyint()
        cls.testPlace = cls.faker.name()[:5]
        cls.listCreateUrl = "/api/tools/setting/"
        cls.retrieveUpdateDestoryUrl = f"/api/tools/setting/{cls.testName}/"

    '''CRUD TEST'''

    def test_tool_올바른_학교_링크로_접속하지_않은_사용자는_교구_목록을_조회할_수_없다(self):
        tools = ToolFactory.create_batch(10, school=self.school)
        toolsList = []
        for tool in tools:
            toolsList.append(dict([
                ('school', self.school.name),
                ('name', tool.name),
                ('quantity', tool.quantity),
                ('place', tool.place)
            ]))
        toolsList = sorted(toolsList, key=lambda x: x['name'])

        response1 = self.client.get(self.listCreateUrl)
        response2 = self.client.get(self.listCreateUrl,
                                    **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response1.status_code, 401)
        self.assertEqual(response2.status_code, 200)
        self.assertNotEqual(response1.data, toolsList)
        self.assertNotEqual(response2.data, toolsList)

    def test_tool_올바른_학교_링크로_접속한_사용자는_교구_목록을_조회할_수_있다(self):
        tools = ToolFactory.create_batch(10, school=self.school)
        toolsList = []
        for tool in tools:
            toolsList.append(dict([
                ('school', self.school.name),
                ('name', tool.name),
                ('quantity', tool.quantity),
                ('place', tool.place)
            ]))
        toolsList = sorted(toolsList, key=lambda x: x['name'])

        response = self.client.get(self.listCreateUrl,
                                   **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, toolsList)

    def test_tool_올바른_학교_링크로_접속하지_않은_사용자는_새로운_교구를_생성할_수_없다(self):
        data = {'name': self.testName, 'quantity': self.testQuantity, 'place': self.testPlace}

        response1 = self.client.post(self.listCreateUrl, data)
        response2 = self.client.post(self.listCreateUrl, data, **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response1.status_code, 401)
        self.assertFalse(Tool.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    def test_tool_올바른_학교_링크로_접속한_사용자는_새로운_교구를_생성할_수_있다(self):
        response = self.client.post(self.listCreateUrl, {
            'name': self.testName,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Tool.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    def test_tool_올바른_학교_링크로_접속하지_않은_사용자는_교구를_조회할_수_없다(self):
        tool = ToolFactory(school=self.school, name=self.testName)
        data = {'school': self.school.name, 'name': tool.name, 'quantity': tool.quantity, 'place': tool.place}

        response1 = self.client.get(self.retrieveUpdateDestoryUrl)
        response2 = self.client.get(self.retrieveUpdateDestoryUrl, **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response1.status_code, 401)
        self.assertNotEqual(response1.data, data)
        self.assertNotEqual(response2.data, data)

    def test_tool_올바른_학교_링크로_접속한_사용자는_교구를_조회할_수_있다(self):
        tool = ToolFactory(school=self.school, name=self.testName)

        response = self.client.get(self.retrieveUpdateDestoryUrl,
                                   **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'school': self.school.name,
            'name': tool.name,
            'quantity': tool.quantity,
            'place': tool.place
        })

    def test_tool_올바른_학교_링크로_접속하지_않은_사용자는_교구를_수정할_수_없다(self):
        tool = ToolFactory(school=self.school, name=self.testName, quantity=80)
        updateData = {'name': tool.name, 'quantity': 10, 'place': self.testPlace}

        response = self.client.put(self.retrieveUpdateDestoryUrl, updateData, content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertNotEqual(Tool.objects.filter(school=self.school.code, name=self.testName).get().quantity, 10)
        self.assertNotEqual(Tool.objects.filter(school=self.school.code, name=self.testName).get().place,
                            self.testPlace)

    def test_tool_올바른_학교_링크로_접속한_사용자는_교구를_수정할_수_있다(self):
        tool = ToolFactory(school=self.school, name=self.testName, quantity=80)
        updateData = {'name': tool.name, 'quantity': 10, 'place': self.testPlace}

        response = self.client.put(self.retrieveUpdateDestoryUrl,
                                   updateData,
                                   content_type='application/json',
                                   **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tool.objects.filter(school=self.school.code, name=self.testName).get().quantity, 10)
        self.assertEqual(Tool.objects.filter(school=self.school.code, name=self.testName).get().place, self.testPlace)

    def test_tool_올바른_학교_링크로_접속하지_않은_사용자는_교구를_삭제할_수_없다(self):
        ToolFactory(school=self.school, name=self.testName)

        response = self.client.delete(self.retrieveUpdateDestoryUrl)

        self.assertEqual(response.status_code, 401)
        self.assertTrue(Tool.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    def test_tool_올바른_학교_링크로_접속한_사용자는_교구를_삭제할_수_있다(self):
        ToolFactory(school=self.school, name=self.testName)

        response = self.client.delete(self.retrieveUpdateDestoryUrl,
                                      **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Tool.objects.filter(
            school=self.school.code,
            name=self.testName
        ).exists())

    '''Validation TEST'''

    def test_tool_학교_코드_내에서_교구_이름은_중복될_수_없다(self):
        tool = ToolFactory(school=self.school, name=self.testName)
        self.assertTrue(
            Tool.objects.filter(school=self.school.code, name=tool.name).exists()
        )

        response = self.client.post(self.listCreateUrl, {
            'name': self.testName,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response.status_code, 400)
        self.assertIn('이미 등록된 이름입니다.', response.data['detail'])

    def test_tool_학교_코드가_다르면_교구_이름은_중복될_수_있다(self):
        tool = ToolFactory(school=self.school, name=self.testName)
        self.assertTrue(
            Tool.objects.filter(school=self.school.code, name=tool.name).exists()
        )

        response = self.client.post(self.listCreateUrl, {
            'name': self.testName,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.otherSchool.code})

        self.assertEqual(response.status_code, 201)

    def test_tool_교구_이름은_5글자_이하이어야_한다(self):
        name5letters = '다섯글자임'
        nameOver5lertters = '여섯글자임다'

        response1 = self.client.post(self.listCreateUrl, {
            'name': name5letters,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})
        response2 = self.client.post(self.listCreateUrl, {
            'name': nameOver5lertters,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertTrue(Tool.objects.filter(school=self.school.code, name=name5letters).exists())
        self.assertFalse(Tool.objects.filter(school=self.school.code, name=nameOver5lertters).exists())

    def test_tool_교구_이름은_특수문자를_포함하지_않아야_한다(self):
        nameWithOutSpecialCharacter = '교구123'
        nameWithSpecialCharacter = '교구12@'

        response1 = self.client.post(self.listCreateUrl, {
            'name': nameWithOutSpecialCharacter,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})
        response2 = self.client.post(self.listCreateUrl, {
            'name': nameWithSpecialCharacter,
            'quantity': self.testQuantity,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertTrue(Tool.objects.filter(school=self.school.code, name=nameWithOutSpecialCharacter).exists())
        self.assertFalse(Tool.objects.filter(school=self.school.code, name=nameWithSpecialCharacter).exists())

    def test_tool_교구_수량은_0_초과이어야_한다(self):
        overZero = randint(1, 100)
        underZero = randint(-100, 0)

        response1 = self.client.post(self.listCreateUrl, {
            'name': self.testName,
            'quantity': overZero,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})
        response2 = self.client.post(self.listCreateUrl, {
            'name': self.faker.name()[:5],
            'quantity': underZero,
            'place': self.testPlace
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertTrue(Tool.objects.filter(school=self.school.code, quantity=overZero).exists())
        self.assertFalse(Tool.objects.filter(school=self.school.code, quantity=underZero).exists())

    def test_tool_교구의_보관_장소는_5글자_이하이어야_한다(self):
        name5letters = '다섯글자임'
        nameOver5lertters = '여섯글자임다'

        response1 = self.client.post(self.listCreateUrl, {
            'name': self.testName,
            'quantity': self.testQuantity,
            'place': name5letters
        }, **{'HTTP_AUTHORIZATION': self.school.code})
        response2 = self.client.post(self.listCreateUrl, {
            'name': self.faker.name()[:5],
            'quantity': self.testQuantity,
            'place': nameOver5lertters
        }, **{'HTTP_AUTHORIZATION': self.school.code})

        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 400)
        self.assertTrue(Tool.objects.filter(school=self.school.code, place=name5letters).exists())
        self.assertFalse(Tool.objects.filter(school=self.school.code, place=nameOver5lertters).exists())
