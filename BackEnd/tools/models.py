from django.db import models

from accounts.models import School


class Tool(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    place = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ToolBooking(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date = models.DateField()
    period = models.PositiveSmallIntegerField()
    booker = models.CharField(max_length=10)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.booker + "(" + str(self.quantity) + "대)"

class LeftQuantity(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    left = models.PositiveSmallIntegerField()
