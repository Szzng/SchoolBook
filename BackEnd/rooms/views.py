from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
import datetime as dt

from .actions import eventsCreated, createEvents, saveTimetable
from .models import Room, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableEvent
from .serializers import RoomBookingSerializer, FixedTimeTableSerializer, RoomSerializer


class RoomListCreate(ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all().order_by('name')

    def create(self, request, *args, **kwargs):
        room, created = Room.objects.get_or_create(name=request.data['room'])
        if created:
            timetable = request.data['timetable']
            saveTimetable(room, timetable)
        return Response(status=status.HTTP_201_CREATED)


class RoomDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        room = Room.objects.get(name=request.data['room'])
        room.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TimetableListCreate(ListCreateAPIView):
    serializer_class = FixedTimeTableSerializer

    def get_queryset(self):
        return FixedTimeTable.objects.all().order_by('room')

    def create(self, request, *args, **kwargs):
        room = Room.objects.get(name=request.data['room'])
        FixedTimeTable.objects.filter(room=room.name).delete()
        EmptyTimeTable.objects.filter(room=room.name).delete()

        timetable = request.data['timetable']
        saveTimetable(room, timetable)

        return Response(status=status.HTTP_201_CREATED)


class TimetableRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        room = Room.objects.get(name=kwargs['room'])
        fixedTimetables = FixedTimeTable.objects.filter(room=room.name).order_by('weekday')
        data = {
            0: ['', '', '', '', '', ''],
            1: ['', '', '', '', '', ''],
            2: ['', '', '', '', '', ''],
            3: ['', '', '', '', '', ''],
            4: ['', '', '', '', '', '']
        }
        for timetable in fixedTimetables:
            data[timetable.weekday][timetable.period - 1] = timetable.booker

        return Response(data)


class RoomBookingListCreate(ListCreateAPIView):
    serializer_class = RoomBookingSerializer

    def get_queryset(self):
        return RoomBooking.objects.all().order_by('date')

    def create(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(request.data['date'], '%Y-%m-%d').weekday()
        emptyTimetable = EmptyTimeTable.objects.get(room=request.data['room'], weekday=weekday,
                                                    period=request.data['period'])
        AvailableEvent.objects.filter(timetable=emptyTimetable, start=request.data['date'],
                                      name=str(request.data['period'])).delete()

        booking = RoomBooking.objects.create(
            timetable=emptyTimetable,
            date=request.data['date'],
            booker=request.data['booker'],
        )
        return Response(self.serializer_class(booking).data)


class RoomBookingRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(kwargs['date'], '%Y-%m-%d').weekday()
        timetable = FixedTimeTable.objects.filter(room=kwargs['room'], weekday=weekday).order_by('period')
        bookings = RoomBooking.objects.filter(date=kwargs['date'])

        data = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
        for booking in bookings:
            data[booking.timetable.period] = {'id': booking.id, 'booker': booking.booker}

        for period in timetable:
            data[period.period] = {'id': 'fixed', 'booker': period.booker}

        return Response(data)


class RoomBookingDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        roomBooking = RoomBooking.objects.get(id=kwargs['bookingId'])
        AvailableEvent.objects.create(
            timetable=roomBooking.timetable,
            start=roomBooking.date,
            name=roomBooking.timetable.period
        )
        roomBooking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AvailableEventByMonthRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        year = kwargs['date'][:4]
        month = kwargs['date'][5:7]
        year_month = year + '-' + month

        if not eventsCreated(kwargs['room'], year_month):
            createEvents(kwargs['room'], year, month)

        events = AvailableEvent.objects.filter(timetable__room=kwargs['room'],
                                               start__contains=year_month).order_by('start').values(
            'name', 'start')

        return Response(events)
