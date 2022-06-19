from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ("ip", "created_at", "updated_at")


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    ip = serializers.CharField(required=True)

    def validate_name(self, name):
        if School.objects.filter(name=name).exists():
            raise ValidationError(_("이미 존재하는 학교 이름입니다. 다른 이름을 사용해주세요."))
        if len(name) < 3:
            raise ValidationError(_("학교 이름은 3글자 이상이어야 합니다."))
        return name

    def validate_ip(self, ip):
        try:
            ip = ".".join(ip.split('.')[:-1])
        except:
            raise ValidationError(_("IP 주소가 올바르지 않습니다. 다시 등록해주세요."))
        return ip

    def save(self):
        school = School(name=self.validated_data["name"], ip=self.validated_data["ip"])
        school.save()
        return school


class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    ip = serializers.CharField(required=True)

    def validate(self, data):
        try:
            school = School.objects.get(name=data['name'])
        except:
            raise ValidationError(_("가입되지 않은 학교 이름입니다."))
        else:
            ip = ".".join(data['ip'].split('.')[:-1])
            if school.ip != ip:
                raise ValidationError(_("IP 주소가 일치하지 않습니다. 학교 컴퓨터를 이용하여 접속해주세요."))
        return school


class JWTSerializer(serializers.Serializer):
    school = serializers.SerializerMethodField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    access_token_expiration = serializers.DateTimeField()
    refresh_token_expiration = serializers.DateTimeField()

    def get_school(self, obj):
        school = SchoolSerializer(obj["school"], context=self.context).data
        return school
