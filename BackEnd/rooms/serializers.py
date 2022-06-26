from rest_framework import serializers

from accounts.serializers import SchoolSerializer


class RoomSerializer(serializers.Serializer):
    school = SchoolSerializer()
    name = serializers.CharField(required=True)


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
    # timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    name = serializers.CharField(required=True)


class RoomBookingSerializer(serializers.Serializer):
    timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    booker = serializers.CharField(required=True)
