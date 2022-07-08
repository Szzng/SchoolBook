from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from accounts.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        read_only_fields = ("code", "created_at", "updated_at")


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

    def validate(self, data):
        if len(data['name']) < 3:
            raise ValidationError({'detail': '학교 이름은 3글자 이상이어야 합니다.'})

        if not data['name'].isalnum():
            raise ValidationError({'detail': '학교 이름에는 특수문자가 포함될 수 없습니다.'})

        return data

    def save(self):
        school = School(name=self.validated_data["name"])
        school.save()
        return school
