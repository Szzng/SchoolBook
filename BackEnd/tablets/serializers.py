from rest_framework import serializers
from .models import TimeTable, BookedTablets, Place


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'
        read_only_fields = ("id",)

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        read_only_fields = ("totalQuantity",)


class BookedTabletsSerializer(serializers.ModelSerializer):
    time = TimeTableSerializer()
    place = PlaceSerializer()

    class Meta:
        model = BookedTablets
        fields = '__all__'
        # depth = 1


