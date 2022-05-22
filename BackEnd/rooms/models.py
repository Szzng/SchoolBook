from django.db import models


class TimeTable(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    period = models.PositiveSmallIntegerField(verbose_name="교시",
                                              choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))


class Place(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class BookedRoom(models.Model):
    time = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    borrower = models.CharField(max_length=100)

    def __str__(self):
        return self.borrower
