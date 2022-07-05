from rest_framework.exceptions import ValidationError
from .models import LeftTool


def getLeft(tool, period):
    leftTool = LeftTool.objects.filter(tool=tool.id, period=period.id)
    if leftTool.exists():
        return leftTool.get().left
    return tool.quantity


def increaseLeft(tool, period, quantity):
    left = getLeft(tool, period) + int(quantity)
    left = min(left, tool.quantity)
    left = max(left, 0)

    LeftTool.objects.update_or_create(
        tool=tool, period=period, defaults={'left': left})


def decreaseLeft(tool, period, quantity):
    left = getLeft(tool, period) - int(quantity)
    
    if left < 0:
        raise ValidationError({'detail': str(period.period) + '교시의 대여 가능한 수량을 확인하세요.'})

    left = min(left, tool.quantity)
    left = max(left, 0)

    LeftTool.objects.update_or_create(
        tool=tool, period=period, defaults={'left': left})

