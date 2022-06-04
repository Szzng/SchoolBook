from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from .models import TimeTable, Place, BookedRoom
from .serializers import BookedRoomSerializer, CreateRoomBookingSerializer


class BookedRoomByDateViewSet(mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = BookedRoomSerializer

    def get_queryset(self):
        data = []
        for i in BookedRoom.objects.all().order_by('time'):
            data.append({
                'id': i.id,
                'name': i.borrower,
                'start': str(i.time.date) + ' ' + str(i.time.period) + ':00',
                'end': str(i.time.date) + ' ' + str(i.time.period+1) + ':00',
            })
        return data

    def create(self, request, *args, **kwargs):
        date, created = TimeTable.objects.get_or_create(
            date=request.data['time.date'],
            period=request.data['time.period'],
            id=request.data['time.date'] + '-' + str(request.data['time.period'])
        )
        place = Place.objects.get(name=request.data['place.name'])
        bookedRoom = BookedRoom.objects.create(
            time=date,
            place=place,
            borrower=request.data['borrower'],
        )

        return Response(CreateRoomBookingSerializer(bookedRoom).data)

    def retrieve(self, request, pk):
        date = TimeTable.objects.filter(id__contains=pk).order_by('id')
        place = Place.objects.filter(name='컴퓨터실1').get()
        data = []
        for period in date:
            dictByPeriod = {
                'name': period.bookedroom_set.filter(place=place.name).get().borrower,
                'start': str(period.date) + ' ' + str(period.period) + ':00',
                'end': str(period.date) + ' ' + str(period.period + 1) + ':00',
            }
            data.append(dictByPeriod)

        return Response(data)

class DestroyBookingViewSet(mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):

    def get_queryset(self):
        pass

    def destroy(self, request, pk, *args, **kwargs):
        roomBooking = BookedRoom.objects.get(id=pk)
        roomBooking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)