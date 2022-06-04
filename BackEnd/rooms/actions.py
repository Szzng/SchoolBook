from .models import Room, EmptyTimeTable, AvailableEvent, RoomBooking, FixedTimeTable
import calendar


def eventsCreated(room, yearMonth):
    events = AvailableEvent.objects.filter(timetable__room=room,
                                           start__contains=yearMonth).exists()
    bookings = RoomBooking.objects.filter(timetable__room=room,
                                          date__contains=yearMonth).exists()

    return events or bookings


def createEvents(room, year, month):
    monthcalendar = calendar.monthcalendar(int(year), int(month))

    for i in range(5):
        emptyPeriodsByWeekDay = EmptyTimeTable.objects.filter(room=room, weekday=i)
        daysOnWeekday = list(map(lambda x: x[i], monthcalendar))
        for day in daysOnWeekday:
            if day == 0: continue
            for emptyPeriod in emptyPeriodsByWeekDay:
                AvailableEvent.objects.create(
                    timetable=emptyPeriod,
                    start=year + '-' + month + '-' + str(day),
                    name=emptyPeriod.period
                )


def saveTimetable(room, timetable):
    for weekday, classlist in timetable.items():
        for period in range(6):
            className = classlist[period]
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
