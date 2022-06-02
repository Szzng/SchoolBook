from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
import datetime as dt
from .models import Place, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableBookingEvent
from .serializers import RoomBookingSerializer, AvailableBookingEventSerializer, FixedTimeTableSerializer, \
    PlaceSerializer
import calendar


class PlacesListCreateAPI(ListCreateAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all().order_by('name')

    def create(self, request, *args, **kwargs):
        for place in request.data['places']:
            if place is not None:
                Place.objects.get_or_create(name=place)

        return Response(Place.objects.all().values('name'))


class PlacesDestroyAPI(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        place = Place.objects.get(name=kwargs['placeName'])
        place.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FixedTimeTableListCreateAPI(ListCreateAPIView):
    serializer_class = FixedTimeTableSerializer

    def get_queryset(self):
        return FixedTimeTable.objects.all().order_by('place')

    def create(self, request, *args, **kwargs):
        place = Place.objects.get(name=request.data['placeName'])
        FixedTimeTable.objects.filter(place=place.name).delete()
        EmptyTimeTable.objects.filter(place=place.name).delete()

        timetable = request.data['fixedTimeTable']
        for weekday, classlist in timetable.items():
            for i in range(6):
                fixedclass = classlist[i]
                if (fixedclass is not None) and (len(fixedclass) >= 1):
                    FixedTimeTable.objects.create(
                        place=place,
                        weekday=weekday,
                        period=i + 1,
                        borrower=fixedclass
                    )
                else:
                    EmptyTimeTable.objects.create(
                        place=place,
                        weekday=weekday,
                        period=i + 1
                    )

        return Response(status=status.HTTP_201_CREATED)


class FixedTimeTableByPlaceAPI(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        place = Place.objects.get(name=kwargs['placeName'])
        timetable = FixedTimeTable.objects.filter(place=place.name).order_by('weekday')
        data = {
            0: ['', '', '', '', '', ''],
            1: ['', '', '', '', '', ''],
            2: ['', '', '', '', '', ''],
            3: ['', '', '', '', '', ''],
            4: ['', '', '', '', '', '']
        }
        for item in timetable:
            data[item.weekday][item.period - 1] = item.borrower

        return Response(data)


class RoomBookingListCreateAPI(ListCreateAPIView):
    serializer_class = RoomBookingSerializer

    def get_queryset(self):
        return RoomBooking.objects.all().order_by('date')

    def create(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(request.data['date'], '%Y-%m-%d').weekday()
        emptyTimetable = EmptyTimeTable.objects.get(place=request.data['placeName'], weekday=weekday,
                                                    period=request.data['period'])
        AvailableBookingEvent.objects.filter(timetable=emptyTimetable, date=request.data['date']).delete()

        booking = RoomBooking.objects.create(
            timetable=emptyTimetable,
            date=request.data['date'],
            borrower=request.data['borrower'],
        )
        return Response(self.serializer_class(booking).data)


class RoomBookingsByDateAPI(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(kwargs['date'], '%Y-%m-%d').weekday()
        fixedTimetable = FixedTimeTable.objects.filter(place=kwargs['placeName'], weekday=weekday).order_by('period')
        bookings = RoomBooking.objects.filter(date=kwargs['date'])

        data = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
        for booking in bookings:
            data[booking.timetable.period] = booking.borrower

        for period in fixedTimetable:
            data[period.period] = period.borrower

        return Response(data)


class RoomBookingDestroyAPI(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        roomBooking = RoomBooking.objects.get(id=kwargs['id'])
        AvailableBookingEvent.objects.create(
            timetable=roomBooking.timetable,
            date=roomBooking.date
        )
        roomBooking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AvailableBookingEventsByMonth(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):

        # 이미 AvailableBookingEvents가 해당 월에 있거나, 룸부킹의 개수가 모두 찬 경우에는 이미 이벤트 생성된 것. -> 바로 get
        AvailableBookingEvent.objects.filter(timetable__place=kwargs['placeName'],
                                             start__contains=kwargs['date'][:-3]).exists()

        # 그외 경우에는 이벤트가 생성되지 않은 상태로 초기 생성 필요 -> 이벤트 생성 후 get
        year = kwargs['date'][:4]
        month = kwargs['date'][5:7]
        monthcalendar = calendar.monthcalendar(year, month)

        for i in range(4):
            emptyPeriodsByWeekDay = EmptyTimeTable.objects.filter(place=kwargs['placeName'], weekday=i)
            daysOnWeekday = list(map(lambda x: x[i], monthcalendar))
            for day in daysOnWeekday:
                if day == 0: continue
                for emptyPeriod in emptyPeriodsByWeekDay:
                    AvailableBookingEvent.objects.create(
                        timetable=emptyPeriod,
                        start=str(year) + '-' + str(month) + '-' + str(day),
                        name=emptyPeriod.period
                    )

        events = AvailableBookingEvent.objects.filter(timetable__place=kwargs['placeName'],
                                                      start__contains=kwargs['date'][:-3]).values('name', 'start')

        return Response(AvailableBookingEventSerializer(events).data)
