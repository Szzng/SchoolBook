from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
import datetime as dt
from .models import Place, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableBooking
from .serializers import RoomBookingSerializer, AvailableBookingSerializer


class RoomBookingListCreateAPI(ListCreateAPIView):
    serializer_class = RoomBookingSerializer

    def get_queryset(self):
        return RoomBooking.objects.all().order_by('date')

    def create(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(request.data['time.date'], '%Y-%m-%d').weekday()
        place = Place.objects.get(name=request.data['place.name'])
        emptyTimetable = EmptyTimeTable.objects.get(place=place.name, weekday=weekday,
                                                    period=request.data['time.period'])
        available = AvailableBooking.objects.get(timetable=emptyTimetable, date=request.data['time.date'])
        available.delete()
        roomBooking = RoomBooking.objects.create(
            timetable=emptyTimetable,
            date=request.data['time.date'],
            borrower=request.data['borrower'],
        )
        return Response(self.serializer_class(roomBooking).data)


class RoomBookingsByDateAPI(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        weekday = dt.datetime.strptime(kwargs['date'], '%Y-%m-%d').weekday()
        place = Place.objects.get(name=kwargs['placeName'])
        fixedTimetable = FixedTimeTable.objects.filter(place=place.name, weekday=weekday).order_by('period')
        roomBookings = RoomBooking.objects.filter(date=kwargs['date']).all()

        data = {}
        for booking in roomBookings:
            data[booking.timetable.period] = booking.borrower

        for period in fixedTimetable:
            data[period.period] = period.borrower

        return Response(data)


class AvailableBookingEventsByMonth(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        place = Place.objects.filter(name=kwargs['placeName']).get()
        date = kwargs['date'][:-3]

        availableEvents = AvailableBooking.objects.filter(timetable__place=place.name,
                                                          date__contains=date).all()
        return Response(AvailableBookingSerializer(availableEvents).data)


class RoomBookingDestroyAPI(DestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        roomBooking = RoomBooking.objects.get(id=kwargs['id'])
        AvailableBooking.objects.create(
            timetable=roomBooking.timetable,
            date=roomBooking.date
        )
        roomBooking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
