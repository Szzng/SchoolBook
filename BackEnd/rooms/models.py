from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class FixedTimeTable(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    weekday = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField()
    booker = models.CharField(max_length=20)


class EmptyTimeTable(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    weekday = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField()


class RoomBooking(models.Model):
    timetable = models.ForeignKey(EmptyTimeTable, on_delete=models.CASCADE)
    date = models.DateField()
    booker = models.CharField(max_length=20)

    def __str__(self):
        return self.booker


class AvailableEvent(models.Model):
    timetable = models.ForeignKey(EmptyTimeTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    start = models.DateField()
