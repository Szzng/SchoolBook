from rest_framework import serializers


class TimeTableSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    date = serializers.DateField(required=True)
    period = serializers.IntegerField(required=True)


class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    totalQuantity = serializers.IntegerField(read_only=True)


class BookedTabletsSerializer(serializers.Serializer):
    time = TimeTableSerializer()
    place = PlaceSerializer()
    borrower = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
