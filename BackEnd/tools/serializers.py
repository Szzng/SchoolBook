from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime as dt

from tools.models import Tool, ToolBooking


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        exclude = ('id',)

    school = serializers.CharField(required=False)

    def validate(self, data):
        school = data.get('school', None)
        if school and Tool.objects.filter(school=school, name=data['name']).exists():
            raise ValidationError({'detail': '이미 등록된 이름입니다.'})

        if len(data['name']) > 5:
            raise ValidationError({'detail': '이름은 5글자 이하로 적어주세요.'})

        if not data['name'].isalnum():
            raise ValidationError({'detail': '이름에는 특수문자가 포함될 수 없습니다.'})

        if data['quantity'] <= 0:
            raise ValidationError({'detail': '수량은 0보다 큰 수를 입력해주세요.'})

        if len(data['place']) > 5:
            raise ValidationError({'detail': '보관 장소는 5글자 이하로 적어주세요.'})
        return data


class ToolBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBooking
        exclude = ('id',)

    tool = serializers.CharField(required=True)
    period = serializers.ListField(required=True)
    date = serializers.CharField(required=True)

    def validate(self, data):
        for i in data['period']:
            if (int(i) <= 0) or (int(i) > 6):
                raise ValidationError({'detail': "예약 교시를 확인하세요."})

        if len(data['booker']) > 4:
            raise ValidationError({'detail': "예약자는 4글자 이하로 적어주세요."})

        if data['quantity'] <= 0:
            raise ValidationError({'detail': '0보다 큰 수를 입력해주세요.'})

        try:
            dt.datetime.strptime(data['date'], '%Y-%m-%d')
        except:
            raise ValidationError({'detail': "날짜 형식이 올바르지 않습니다."})

        return data
