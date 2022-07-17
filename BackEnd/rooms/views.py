from django.utils.decorators import method_decorator
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import datetime as dt
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
class TimetableCreate(CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = RoomTimetableSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        room = get_object_or_404(Room, **{'school': request.user, 'name': data['room']})
        FixedTimeTable.objects.filter(room=room.id).delete()
        EmptyTimeTable.objects.filter(room=room.id).delete()
        CreatedEvents.objects.filter(room=room.id).delete()

        timetable = data['timetable']
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
    def create(self, request, *args, **kwargs):
        serializer = RoomBookingCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        weekday = dt.datetime.strptime(data['date'], '%Y-%m-%d').weekday()
        room = get_object_or_404(Room, **{'school': request.user, 'name': data['room']})

        emptyTimetable = get_object_or_404(EmptyTimeTable, **{
            'room': room.id,
            'weekday': weekday,
            'period': data['period']
        })

        try:
            RoomBooking.objects.get(timetable=emptyTimetable, date=data['date'])
            return Response(
                data={'detail': '이미 예약 완료된 시간입니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            booking = RoomBooking.objects.create(
                timetable=emptyTimetable,
                date=data['date'],
                booker=data['booker'],
            )

            AvailableEvent.objects.filter(
                timetable=emptyTimetable,
                start=data['date'],
                name=str(data['period'])
            ).delete()

        return Response(RoomBookingSerializer(booking).data)


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
