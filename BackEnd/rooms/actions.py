from .models import Place, EmptyTimeTable, AvailableBookingEvent, RoomBooking, FixedTimeTable
import calendar


def eventsCreated(placeName, yearMonth):
    events = AvailableBookingEvent.objects.filter(timetable__place=placeName,
                                                  start__contains=yearMonth).exists()
    bookings = RoomBooking.objects.filter(timetable__place=placeName,
                                          date__contains=yearMonth).exists()

    return events or bookings


def createEvents(place, year, month):
    monthcalendar = calendar.monthcalendar(int(year), int(month))

    for i in range(5):
        emptyPeriodsByWeekDay = EmptyTimeTable.objects.filter(place=place, weekday=i)
        daysOnWeekday = list(map(lambda x: x[i], monthcalendar))
        for day in daysOnWeekday:
            if day == 0: continue
            for emptyPeriod in emptyPeriodsByWeekDay:
                AvailableBookingEvent.objects.create(
                    timetable=emptyPeriod,
                    start=year + '-' + month + '-' + str(day),
                    name=emptyPeriod.period
                )


def saveTimetable(place, timetable):
    for weekday, classlist in timetable.items():
        for period in range(6):
            className = classlist[period]
            if (className is not None) and (len(className) >= 1):
                FixedTimeTable.objects.create(
                    place=place,
                    weekday=weekday,
                    period=period + 1,
                    borrower=className
                )
            else:
                EmptyTimeTable.objects.create(
                    place=place,
                    weekday=weekday,
                    period=period + 1
                )
