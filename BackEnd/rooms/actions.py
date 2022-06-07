from .models import EmptyTimeTable, AvailableEvent, RoomBooking, FixedTimeTable
import calendar


def eventsCreated(room, year_month):
    events = AvailableEvent.objects.filter(timetable__room=room,
                                           start__contains=year_month).exists()
    bookings = RoomBooking.objects.filter(timetable__room=room,
                                          date__contains=year_month).exists()

    return events or bookings


def createEvents(room, year, month):
    monthcalendar = calendar.monthcalendar(int(year), int(month))

    for weekday in range(5):
        emptyPeriodsByWeekDay = EmptyTimeTable.objects.filter(room=room, weekday=weekday)
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
    for weekday, classList in timetable.items():
        for period in range(6):
            className = classList[period]
            if (className is not None) and (len(className) >= 1):
                FixedTimeTable.objects.create(
                    room=room,
                    weekday=weekday,
                    period=period + 1,
                    booker=className
                )
            else:
                EmptyTimeTable.objects.create(
                    room=room,
                    weekday=weekday,
                    period=period + 1
                )
