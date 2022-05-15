from django.db import models


class TimeTable(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    period = models.PositiveSmallIntegerField(verbose_name="교시",
                                              choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))

class BookedTablets(models.Model):
    time = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    place = models.CharField(max_length=100, choices=(('전산실', '전산실'), ('학습 준비물실', '학습 준비물실')))
    borrower = models.CharField(max_length=100)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.borrower + "(" + str(self.quantity) + "대)"
