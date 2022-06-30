from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import School
from .serializers import RegisterSerializer, SchoolSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        school = serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data={'name': school.name, 'code': school.code},
        )


class LoginView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        try:
            school = School.objects.get(code=kwargs['pk'])
            return Response(
                data={'name': school.name, 'code': school.code},
                status=status.HTTP_201_CREATED,
            )

        except School.DoesNotExist:
            return Response(
                data={'detail': '정보를 찾을 수 없습니다. 학교 고유 링크를 확인하세요.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
