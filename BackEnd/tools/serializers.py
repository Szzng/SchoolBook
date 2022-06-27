from rest_framework import serializers

from accounts.serializers import SchoolSerializer
from tools.models import Tool, Period


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class ToolBookingSerializer(serializers.Serializer):
    tool = ToolSerializer()
    period = PeriodSerializer()
    booker = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
