from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView

from .decorators import assert_login
from .serializers import RegisterSerializer, LoginSerializer, JWTSerializer, SchoolSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        self.request.data['ip'] = request.META.get("REMOTE_ADDR", '')
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        school = serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(
            status=status.HTTP_201_CREATED,
            data={'name': school.name, 'ip': school.ip},
            headers=headers
        )


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    school = None
    access_token = None
    access_token_expiration = timezone.now() + timedelta(hours=2)
    refresh_token = None
    refresh_token_expiration = timezone.now() + timedelta(days=7)

    def generate_jwt_token(self):
        access_payload = {"name": self.school.name, "exp": self.access_token_expiration}
        self.access_token = jwt.encode(
            access_payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )

        refresh_payload = {"name": self.school.name, "exp": self.refresh_token_expiration}
        self.refresh_token = jwt.encode(
            refresh_payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )

    def get_response(self):
        data = {
            "access_token": self.access_token,
            "access_token_expiration": self.access_token_expiration,
            "refresh_token": self.refresh_token,
            "refresh_token_expiration": self.refresh_token_expiration,
        }
        serializer = JWTSerializer(data, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request.data['ip'] = request.META["REMOTE_ADDR"]
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.school = serializer.validated_data
        self.generate_jwt_token()

        return self.get_response()


class LogoutView(GenericAPIView):
    @assert_login
    def get(self, request):
        return Response(status=status.HTTP_202_ACCEPTED)


class SchoolDetail(APIView):
    @assert_login
    def get(self, request):
        serializer = SchoolSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
