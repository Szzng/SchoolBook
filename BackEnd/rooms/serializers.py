from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class FixedTimeTableSerializer(serializers.Serializer):
    place = RoomSerializer()
    weekday = serializers.IntegerField(required=True)
    period = serializers.IntegerField(required=True)
    borrower = serializers.CharField(required=True)


class EmptyTimeTableSerializer(serializers.Serializer):
    place = RoomSerializer()
    weekday = serializers.IntegerField(required=True)
    period = serializers.IntegerField(required=True)


class AvailableEventSerializer(serializers.Serializer):
    # timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    name = serializers.CharField(required=True)


class RoomBookingSerializer(serializers.Serializer):
    timetable = EmptyTimeTableSerializer()
    date = serializers.DateField(required=True)
    borrower = serializers.CharField(required=True)
