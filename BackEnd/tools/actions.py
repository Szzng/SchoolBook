from rest_framework.exceptions import ValidationError
from .models import LeftQuantity


def getLeft(tool, time):
    left, created = LeftQuantity.objects.get_or_create(
        tool=tool,
        time=time,
        defaults={'left': tool.quantity}
    )
    return left.left


def increaseLeft(tool, time, quantity):
    left = getLeft(tool, time) + int(quantity)
    left = min(left, tool.quantity)
    left = max(left, 0)

    LeftQuantity.objects.update_or_create(
        tool=tool,
        time=time,
        defaults={'left': left}
    )


def decreaseLeft(tool, time, quantity):
    left = getLeft(tool, time) - int(quantity)

    if left < 0:
        raise ValidationError({
            'detail': str(time[-1]) + '교시의 대여 가능한 수량을 확인하세요.'
        })

    left = min(left, tool.quantity)
    left = max(left, 0)

    LeftQuantity.objects.update_or_create(
        tool=tool,
        time=time,
        defaults={'left': left}
    )
