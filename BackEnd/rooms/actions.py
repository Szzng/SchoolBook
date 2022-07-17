from .models import EmptyTimeTable, AvailableEvent, FixedTimeTable, CreatedEvents
import calendar


def createEvents(room, year, month, year_month):
    if CreatedEvents.objects.filter(room=room.id, date=year_month).exists():
        return

    CreatedEvents.objects.create(room=room, date=year_month)

    monthcalendar = calendar.monthcalendar(int(year), int(month))

    for weekday in range(5):
        emptyPeriodsByWeekDay = EmptyTimeTable.objects.filter(room=room.id, weekday=weekday)
        daysOnWeekday = list(map(lambda x: x[weekday], monthcalendar))

        for day in daysOnWeekday:
            if day == 0: continue
            for emptyPeriod in emptyPeriodsByWeekDay:
                AvailableEvent.objects.create(
                    timetable=emptyPeriod,
                    name=emptyPeriod.period,
                    start=year + '-' + month + '-' + str(day)
                )


def saveTimetable(room, timetable):
    for weekday, classes in timetable.items():
        for period in range(6):
            booker = classes[period]
            if (booker is not None) and (len(booker) >= 1):
                FixedTimeTable.objects.create(
                    room=room,
                    weekday=weekday,
                    period=period + 1,
                    booker=booker
                )
            else:
                EmptyTimeTable.objects.create(
                    room=room,
                    weekday=weekday,
                    period=period + 1
                )
