from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
import datetime as dt
from .models import Place, RoomBooking, FixedTimeTable, EmptyTimeTable, AvailableBooking
from .serializers import RoomBookingSerializer, AvailableBookingSerializer, FixedTimeTableSerializer, PlaceSerializer


class SetPlacesListCreateAPI(ListCreateAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.all().order_by('name')

    def create(self, request, *args, **kwargs):
        for place in request.data['places']:
            if place is not None:
                Place.objects.get_or_create(name=place)

        return Response(Place.objects.all().values('name'))


class SetPlacesDestroyAPI(DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        place = Place.objects.get(name=kwargs['placeName'])
        place.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class SetFixedTimeTableListCreateAPI(ListCreateAPIView):
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


class SetFixedTimeTableByPlaceAPI(RetrieveAPIView):
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
        weekday = dt.datetime.strptime(request.data['time.date'], '%Y-%m-%d').weekday()
        place = Place.objects.get(name=request.data['placeName'])
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
