from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from .models import TimeTable, Place, BookedTablets, LeftTablets
from .serializers import BookedTabletsSerializer
from .actions import updateLeftTabletsCount, getLeftTabletsCount


class BookedTabletsListCreateAPI(ListCreateAPIView):
    serializer_class = BookedTabletsSerializer

    def get_queryset(self):
        return BookedTablets.objects.all().order_by('time')

    def create(self, request, *args, **kwargs):
        for i in request.data['time.period']:
            date, created = TimeTable.objects.get_or_create(
                date=request.data['time.date'],
                period=i,
                id=request.data['time.date'] + '-' + str(i)
            )
            place = Place.objects.get(name=request.data['place.name'])
            bookedTablets = BookedTablets.objects.create(
                time=date,
                place=place,
                borrower=request.data['borrower'],
                quantity=request.data['quantity']
            )
            updateLeftTabletsCount(
                time=date,
                place=place,
                count=request.data['quantity'],
                increase=False
            )

        return Response(self.serializer_class(bookedTablets).data)


class BookedTabletsByDateAPI(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        timetable = TimeTable.objects.filter(id__contains=kwargs['date']).order_by('id')
        place = Place.objects.filter(name=kwargs['placeName']).get()
        data = {}

        for period in timetable:
            data[period.period] = list(
                period.bookedtablets_set.filter(place=place.name).values('id', 'borrower', 'quantity'))
        return Response(data)


class BookedTabletsDestroyAPI(DestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        bookedTablet = BookedTablets.objects.get(id=kwargs['id'])
        updateLeftTabletsCount(
            time=bookedTablet.time,
            place=bookedTablet.place,
            count=bookedTablet.quantity,
            increase=True
        )
        bookedTablet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LeftTabletsCountAPI(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        timetable = TimeTable.objects.filter(id__contains=kwargs['date']).order_by('id')
        place = Place.objects.filter(name=kwargs['placeName']).get()

        lefts = [place.totalQuantity] * 6
        for period in timetable:
            lefts[period.period - 1] = getLeftTabletsCount(period, place)

        return Response(lefts)
