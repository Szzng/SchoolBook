from .models import Place, EmptyTimeTable, AvailableBooking
import calendar


def initialize(year):
    for place in Place.objects.all():
        emptytimetables = EmptyTimeTable.objects.filter(place=place.name).order_by('weekday')
        createAvailableBooking(emptytimetables, year, 3, 13)
        createAvailableBooking(emptytimetables, year + 1, 1, 3)


def createAvailableBooking(emptytimetables, year, start, end):
    for month in range(start, end):
        for empty in emptytimetables:
            days = list(map(lambda x: x[empty.weekday], calendar.monthcalendar(year, month)))
            for day in days:
                if day == 0:
                    continue
                AvailableBooking.objects.create(
                    timetable=empty,
                    date=str(year) + '-' + str(month) + '-' + str(day)
                )