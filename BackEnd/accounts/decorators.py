from rest_framework import status
from rest_framework.response import Response
from accounts.models import School


def assert_school_code(func):
    def wrapper(self, *args, **kwargs):
        code = self.META.get('HTTP_AUTHORIZATION', None)

        if code is None:
            return Response(
                data={'detail': '학교 고유 링크로 접속하세요.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        try:
            school = School.objects.get(code=code)
            self.user = school
            return func(self, *args, **kwargs)

        except School.DoesNotExist:
            return Response(
                data={'detail': '정보를 찾을 수 없습니다. 학교 고유 링크를 확인하세요.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

    return wrapper
