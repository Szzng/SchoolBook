from rest_framework import serializers
from .models import TimeTable, BookedTablets


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'
        read_only_fields = ("id",)

class BookedTabletsSerializer(serializers.ModelSerializer):
    time = TimeTableSerializer()

    class Meta:
        model = BookedTablets
        fields = '__all__'
        # depth = 1


def obj_to_tablets(obj):
    tablets = dict(vars(obj))


