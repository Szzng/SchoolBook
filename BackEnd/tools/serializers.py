from rest_framework import serializers


class ToolSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
    place = serializers.CharField(required=True)


class PeriodSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    date = serializers.DateField(required=True)
    period = serializers.IntegerField(required=True)


class ToolBookingSerializer(serializers.Serializer):
    tool = ToolSerializer()
    period = PeriodSerializer()
    booker = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
