from django.db import models

from accounts.models import School


class Room(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

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
    password = models.CharField(max_length=4, default='0000')

    def __str__(self):
        return self.booker


class CreatedEvents(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)


class AvailableEvent(models.Model):
    timetable = models.ForeignKey(EmptyTimeTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    start = models.DateField()

    def __str__(self):
        return str(self.start) + '-' + self.name