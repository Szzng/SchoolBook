from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ("code", "created_at", "is_active")


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    password1 = serializers.CharField(style={"input_type": "password"})
    password2 = serializers.CharField(style={"input_type": "password"})
    write_only_fields = ("password1", "password2")

    def validate_password1(self, password):
        min_length = 6
        if len(password) < min_length:
            raise ValidationError(_("비밀번호는 최소 {0}자 이상으로 만들어주세요.").format(min_length))
        validate_password(password)
        return password

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise ValidationError(_("두 비밀번호가 일치하지 않습니다."))
        return data

    def get_cleaned_data(self):
        return {
            "name": self.validated_data.get("name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

    def save(self):
        data = self.get_cleaned_data()
        school = School.objects.create_user(
            name=data["name"],
            password=data["password1"]
        )
        school.save()
        return school


class LoginSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    password = serializers.CharField(style={"input_type": "password"})

    def authenticate(self, **kwargs):
        return authenticate(self.context["request"], **kwargs)

    def validate(self, data):
        code = data["code"]
        password = data["password"]

        if code and password:
            school = self.authenticate(code=code, password=password)
        else:
            msg = _("학교 코드와 비밀번호를 입력해주세요.")
            raise ValidationError(msg)

        if not school:
            msg = _("일치하는 학교 회원 계정을 찾을 수 없습니다.")
            raise ValidationError(msg)

        if not school.is_active:
            msg = _("정지된 회원 계정입니다.")
            raise ValidationError(msg)

        data["school"] = school
        return data


class SchoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ("name", "code", "is_active")
        read_only_fields = (
            "code",
            "is_active",
        )


class JWTSerializer(serializers.Serializer):
    school = serializers.SerializerMethodField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    access_token_expiration = serializers.DateTimeField()
    refresh_token_expiration = serializers.DateTimeField()

    def get_school(self, obj):
        school_data = SchoolDetailSerializer(obj["school"], context=self.context).data
        return school_data
