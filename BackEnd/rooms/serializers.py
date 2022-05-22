from rest_framework import serializers


class TimeTableSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    date = serializers.DateField(required=True)
    period = serializers.IntegerField(required=True)


class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)


class CreateRoomBookingSerializer(serializers.Serializer):
    time = TimeTableSerializer()
    place = PlaceSerializer()
    borrower = serializers.CharField(required=True)

class BookedRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    start = serializers.CharField()
    end = serializers.CharField()