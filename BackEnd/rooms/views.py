from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from datetime import datetime as dt
from accounts.decorators import assert_school_code
from .actions import createEvents, saveTimetable
from .models import Room, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableEvent, CreatedEvents
from .serializers import RoomBookingSerializer, RoomSerializer, RoomTimetableSerializer, RoomBookingCreateSerializer


@method_decorator(assert_school_code, name='list')
@method_decorator(assert_school_code, name='create')
class RoomListCreate(ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.filter(school=self.request.user.code).order_by('name')

    def create(self, request, *args, **kwargs):
        requestData = self.request.data.copy()
        requestData['school'] = request.user.code
        serializer = RoomTimetableSerializer(data=requestData)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        room = Room.objects.create(
            school=request.user,
            name=data['room']
        )
        saveTimetable(room, data['timetable'])

        return Response(status=status.HTTP_201_CREATED)


@method_decorator(assert_school_code, name='destroy')
class RoomDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': request.data['room']})
        room.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(assert_school_code, name='create')
class TimetableUpdate(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = RoomTimetableSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        room = get_object_or_404(Room, **{'school': request.user, 'name': data['room']})
        FixedTimeTable.objects.filter(room=room.id).delete()
        EmptyTimeTable.objects.filter(room=room.id).delete()
        CreatedEvents.objects.filter(room=room.id).delete()

        saveTimetable(room, data['timetable'])
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
    def create(self, request, *args, **kwargs):
        requestData = self.request.data.copy()
        requestData['school'] = request.user.code
        serializer = RoomBookingCreateSerializer(data=requestData)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        booking = RoomBooking.objects.create(
            timetable=data['emptyTimetable'],
            date=data['date'],
            booker=data['booker'],
            password=data['password']
        )

        AvailableEvent.objects.filter(
            timetable=data['emptyTimetable'],
            start=data['date'],
            name=str(data['period'])
        ).delete()

        return Response(status=status.HTTP_201_CREATED, data=RoomBookingSerializer(booking).data)


@method_decorator(assert_school_code, name='retrieve')
class RoomBookingByDate(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': kwargs['room']})
        data = {1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}

        bookings = RoomBooking.objects.filter(timetable__room_id=room.id, date=kwargs['date'])
        for booking in bookings:
            data[booking.timetable.period] = {'id': booking.id, 'booker': booking.booker}

        fixedTimetable = FixedTimeTable.objects.filter(
            room=room.id,
            weekday=dt.strptime(kwargs['date'], '%Y-%m-%d').weekday()
        ).order_by('period')
        for period in fixedTimetable:
            data[period.period] = {'id': 'fixed', 'booker': period.booker}

        return Response(data)


@method_decorator(assert_school_code, name='destroy')
class RoomBookingDestroy(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        booking = get_object_or_404(RoomBooking, id=kwargs['bookingId'])

        if booking.password != request.data['password']:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'detail': '잘못된 비밀번호입니다.'})

        AvailableEvent.objects.create(
            timetable=booking.timetable,
            start=booking.date,
            name=booking.timetable.period
        )
        booking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(assert_school_code, name='retrieve')
class AvailableEventByMonth(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        room = get_object_or_404(Room, **{'school': request.user, 'name': kwargs['room']})
        year = kwargs['date'][:4]
        month = kwargs['date'][5:7]
        year_month = year + '-' + month
        createEvents(room, year, month, year_month)

        events = AvailableEvent.objects.filter(
            timetable__room=room.id,
            start__contains=year_month
        ).order_by('start').values('name', 'start')

        return Response(events)
