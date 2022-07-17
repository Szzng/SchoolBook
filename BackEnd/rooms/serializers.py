from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import datetime as dt

from rooms.models import Room


class RoomSerializer(serializers.Serializer):
    school = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class RoomTimetableSerializer(serializers.Serializer):
    school = serializers.CharField(required=False)
    room = serializers.CharField(required=True)
    timetable = serializers.DictField(required=True, child=serializers.ListField())

    def validate(self, data):
        school = data.get('school', None)
        if school and Room.objects.filter(school=school, name=data['room']).exists():
            raise ValidationError({'detail': '이미 등록된 이름입니다.'})

        if len(data['room']) > 5:
            raise ValidationError({'detail': "이름은 5글자 이하로 적어주세요."})

        if not data['room'].isalnum():
            raise ValidationError({'detail': '이름에는 특수문자가 포함될 수 없습니다.'})

        if len(data['timetable']) != 5:
            raise ValidationError({'detail': '시간표 형식이 올바르지 않습니다.'})

        for i in data['timetable'].values():
            if len(i) != 6:
                raise ValidationError({'detail': '시간표 형식이 올바르지 않습니다.'})
        return data


class EmptyTimeTableSerializer(serializers.Serializer):
    room = RoomSerializer()
    weekday = serializers.IntegerField(required=True)
    period = serializers.IntegerField(required=True)


class AvailableEventSerializer(serializers.Serializer):
    date = serializers.DateField(required=True)
    name = serializers.CharField(required=True)


class RoomBookingCreateSerializer(serializers.Serializer):
    date = serializers.CharField(required=True)
    period = serializers.IntegerField(required=True)
    room = serializers.CharField(required=True)
    booker = serializers.CharField(required=True)

    def validate(self, data):
        if (data['period'] <= 0) or (data['period'] > 6):
            raise ValidationError({'detail': "예약 교시를 확인하세요."})

        try:
            dt.datetime.strptime(data['date'], '%Y-%m-%d')
        except:
            raise ValidationError({'detail': "날짜 형식이 올바르지 않습니다."})

        if len(data['booker']) > 4:
            raise ValidationError({'detail': "예약자는 4글자 이하로 적어주세요."})
        return data


class RoomBookingSerializer(serializers.Serializer):
    timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    booker = serializers.CharField(required=True)
