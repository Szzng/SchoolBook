from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class RoomSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class RoomTimetableSerializer(serializers.Serializer):
    room = serializers.CharField(required=True)
    timetable = serializers.DictField(required=True, child=serializers.ListField())

    def validate(self, data):
        if len(data['room']) > 5:
            raise ValidationError({'detail': "이름은 5글자 이하로 적어주세요."})

        if len(data['timetable']) != 5:
            raise ValidationError({'detail': '시간표 형식이 올바르지 않습니다.'})

        for i in data['timetable'].values():
            if len(i) != 6:
                raise ValidationError({'detail': '시간표 형식이 올바르지 않습니다.'})
        return data


class FixedTimeTableSerializer(serializers.Serializer):
    room = RoomSerializer()
    weekday = serializers.IntegerField(required=True)
    period = serializers.IntegerField(required=True)
    booker = serializers.CharField(required=True)


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
        if len(data['booker']) > 4:
            raise ValidationError({'detail': "예약자는 4글자 이하로 적어주세요."})
        return data

class RoomBookingSerializer(serializers.Serializer):
    timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    booker = serializers.CharField(required=True)

