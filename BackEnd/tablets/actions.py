from .models import LeftTablets


def getLeftTabletsCount(time, place):
    leftObject = LeftTablets.objects.filter(time=time.id, place=place.name)

    if leftObject.exists():
        left = leftObject.get().count
    else:
        left = place.totalQuantity

    return left


def updateLeftTabletsCount(time, place, count, increase=True):
    left = getLeftTabletsCount(time, place)

    if increase:
        left += int(count)
    else:
        left -= int(count)

    LeftTablets.objects.update_or_create(
        time=time, place=place,
        defaults={'count': left}
    )
