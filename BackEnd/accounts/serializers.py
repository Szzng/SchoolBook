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

    def validate_name(self, name):
        if len(name) < 3:
            raise ValidationError({'detail': '학교 이름은 3글자 이상이어야 합니다.'})
        return name

    def save(self):
        school = School(name=self.validated_data["name"])
        school.save()
        return school
