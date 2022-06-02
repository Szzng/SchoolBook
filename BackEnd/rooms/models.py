from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class FixedTimeTable(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    weekday = models.PositiveSmallIntegerField(verbose_name="요일",
                                               choices=((0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금')))
    period = models.PositiveSmallIntegerField(verbose_name="교시",
                                              choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))
    borrower = models.CharField(max_length=100)


class EmptyTimeTable(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    weekday = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField(verbose_name="교시",
                                              choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))


class AvailableBookingEvent(models.Model):
    timetable = models.ForeignKey(EmptyTimeTable, on_delete=models.CASCADE)
    start = models.DateField()
    name = models.PositiveSmallIntegerField()


class RoomBooking(models.Model):
    timetable = models.ForeignKey(EmptyTimeTable, on_delete=models.CASCADE)
    date = models.DateField()
    borrower = models.CharField(max_length=100)

    def __str__(self):
        return self.borrower
