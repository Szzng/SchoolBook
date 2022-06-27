from django.db import models

from accounts.models import School


class Tool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Period(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()
    period = models.PositiveSmallIntegerField(verbose_name="교시",
                                              choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))

class ToolBooking(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    booker = models.CharField(max_length=10)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.booker + "(" + str(self.quantity) + "대)"

class LeftTool(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    left = models.PositiveSmallIntegerField()
