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
        headers = self.get_success_headers(serializer.data)

        return Response(
            status=status.HTTP_201_CREATED,
            data={'name': school.name, 'code': school.code},
            headers=headers
        )

class LoginView(RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
