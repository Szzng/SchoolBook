from .models import Place, EmptyTimeTable, AvailableBookingEvent, RoomBooking
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
