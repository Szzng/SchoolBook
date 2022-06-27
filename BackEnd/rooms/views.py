from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import datetime as dt

from accounts.decorators import assert_school_code
from .actions import eventsCreated, createEvents, saveTimetable
from .models import Room, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableEvent
from .serializers import RoomBookingSerializer, FixedTimeTableSerializer, RoomSerializer


@method_decorator(assert_school_code, name='list')
@method_decorator(assert_school_code, name='create')
class RoomListCreate(ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(school=self.request.user.code).order_by('name')

    def create(self, request, *args, **kwargs):
        if Room.objects.filter(school=request.user, name=request.data['room']).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        room = Room.objects.create(
            school=request.user,
            name=request.data['room']
        )
        saveTimetable(room, request.data['timetable'])

        return Response(status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='destroy')
class RoomDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': request.data['room']})
        room.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(assert_school_code, name='create')
class TimetableCreate(CreateAPIView):
    serializer_class = FixedTimeTableSerializer

    def create(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': request.data['room']})
        FixedTimeTable.objects.filter(room=room.id).delete()
        EmptyTimeTable.objects.filter(room=room.id).delete()

        timetable = request.data['timetable']
        saveTimetable(room, timetable)
        return Response(status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='retrieve')
class TimetableRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': kwargs['room']})
        fixedTimetables = FixedTimeTable.objects.filter(room=room.id).order_by('weekday')
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


@method_decorator(assert_school_code, name='create')
class RoomBookingCreate(CreateAPIView):
    serializer_class = RoomBookingSerializer

    def create(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(request.data['date'], '%Y-%m-%d').weekday()
        room = get_object_or_404(Room, **{'school': request.user, 'name': request.data['room']})

        emptyTimetable = EmptyTimeTable.objects.get(
            room=room.id,
            weekday=weekday,
            period=request.data['period']
        )

        AvailableEvent.objects.filter(
            timetable=emptyTimetable,
            start=request.data['date'],
            name=str(request.data['period'])
        ).delete()

        booking = RoomBooking.objects.create(
            timetable=emptyTimetable,
            date=request.data['date'],
            booker=request.data['booker'],
        )
        return Response(self.serializer_class(booking).data)


@method_decorator(assert_school_code, name='retrieve')
class RoomBookingRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(kwargs['date'], '%Y-%m-%d').weekday()
        room = get_object_or_404(Room, **{'school': request.user, 'name': kwargs['room']})
        timetable = FixedTimeTable.objects.filter(room=room.id, weekday=weekday).order_by('period')
        bookings = RoomBooking.objects.filter(timetable__room_id=room.id, date=kwargs['date'])

        data = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
        for booking in bookings:
            data[booking.timetable.period] = {'id': booking.id, 'booker': booking.booker}

        for period in timetable:
            data[period.period] = {'id': 'fixed', 'booker': period.booker}

        return Response(data)


@method_decorator(assert_school_code, name='destroy')
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

@method_decorator(assert_school_code, name='retrieve')
class AvailableEventByMonthRetrieve(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        year = kwargs['date'][:4]
        month = kwargs['date'][5:7]
        year_month = year + '-' + month
        room = get_object_or_404(Room, **{'school': request.user, 'name': kwargs['room']})

        if not eventsCreated(room, year_month):
            createEvents(room, year, month)

        events = AvailableEvent.objects.filter(
            timetable__room=room.id,
            start__contains=year_month
        ).order_by('start').values('name', 'start')

        return Response(events)
